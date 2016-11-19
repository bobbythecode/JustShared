import os
import sys
import json
 
from flask import Flask, jsonify
from flask import request, Response 
from flask import render_template
from flask import redirect, url_for
from flask import send_from_directory

from handler import ProcessRequest

from playhouse.shortcuts import model_to_dict, dict_to_model
from werkzeug import secure_filename

from common.config import *
from common.helpers import *
from common.enums import *
from common.constants import *

from common.errors import *

from model.entities.partnerEntity import *

#===============================================================
# Global Variables Initialization
#===============================================================

app = Flask(__name__, static_folder='static', static_url_path='')
               
setUploadConfigs(app)
               
#################################################################

@app.route('/')
def index():
    return redirect(url_for('view'))

#-----------------------------------------------------------------

@app.route('/read/<name>')
def read(name):
    try:
        resp = ProcessRequest().read(name)
        resp = json.dumps(model_to_dict(resp))
        
        resp = Response(resp, status=HttpStatus.OK, mimetype='application/json')
        return resp
        
    except:
        return returnInternalError();        
         

#-----------------------------------------------------------------

@app.route('/create/<name>/<slug>/<active>/<path:spread_sheet_path>/<path:image_path>', methods=['GET', 'POST'])
def create(name, slug=None, active=True, spread_sheet_path=None, image_path=None):
    try:
        active = active == 'True'            
        ProcessRequest().create(name, slug, active, spread_sheet_path, image_path)
        
        return returnSuccess();        

    except:
        return returnInternalError();        
        raise
        
#-----------------------------------------------------------------

@app.route('/update/<name>/<slug>/<active>/<path:spread_sheet_path>/<path:image_path>', methods=['GET'])
def update(name, slug, active, spread_sheet_path, image_path):
    try:
        active = active == 'True'            
        ProcessRequest().update(name, slug, active, spread_sheet_path, image_path)

        return returnSuccess();        

    except:
        return returnInternalError();        
        raise
        
#-----------------------------------------------------------------

@app.route('/delete/<name>', methods=['GET'])
def delete(name):
    try:
        ProcessRequest().delete(name)        
        return returnSuccess();        

    except:
        return returnInternalError();        
        raise

#-----------------------------------------------------------------

@app.route('/view', methods=['GET'])
def view():
    try:
        partners = ProcessRequest().readAll()                
        return render_template('view-all.html', root='update-partner/', list=partners)    

    except NotFoundError as e:
        return redirect(url_for('updatePartner'))

    except:
        return returnInternalError();        
        raise

@app.route('/edit/<name>', methods=['GET'])
def edit(name):
    try:
        typeSet = getTypes(app);
        partner = ProcessRequest().read(name)                
        return render_template('update-form.html', partner=partner, typeSet=typeSet)

    except NotFoundError as e:
        return redirect(url_for('updatePartner'))

    except:
        return returnInternalError();        
        raise
        
#-----------------------------------------------------------------

@app.route('/update-partner', methods=['GET','POST'])
@app.route('/edit/update-partner', methods=['POST'])
def updatePartner():
    try:
        if request.method == 'POST':
            name = request.form['name']
            slug = request.form['slug']
            active = request.form['active']

            active = active.lower() == 'true'            
            spread_sheet_path = None
            image_path = None
            
            redir = None
    
            file = request.files['file']
            if file.filename:        
                if file and __allowedFile__(file.filename):
                    filename = secure_filename(file.filename)
                    
                    path = getFolderExt(app, filename);
                    tmp = os.path.join(app.config['UPLOAD_FOLDER'], path)
                    if not os.path.isdir(tmp):
                        os.makedirs(tmp)
                        
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], path, filename))
                    
                    redir = path + "/" + filename
                    
                    t = getFolderType(app, filename);
                    if t == 'sheet':
                        spread_sheet_path = redir;
                        
                    elif t == 'image':
                        image_path = redir     
                    
            
            ProcessRequest().create(name, slug, active, spread_sheet_path, image_path)
            
            if redir:
                return redirect(url_for('view', filename=redir))
            
            return redirect(url_for('index'))
        
        
        else:            
            typeSet = getTypes(app);
            
            partner = Partner()
            partner.name = ''
            partner.slug = ''
            return render_template('update-form.html', partner=partner, typeSet=typeSet)


    except:
        return returnInternalError();        
        raise

#-----------------------------------------------------------------
        
@app.route('/update-partner/<path:filename>')
def showPartner(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    except:
        return returnInternalError();        
        raise
                 
@app.after_request
def after_request(response):
    response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
    return response                            
#-----------------------------------------------------------------
                            
def __allowedFile__(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
            
            
#############################################################

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page-not-found.html'), 404


#############################################################

if __name__ == '__main__':
    app.run(
        host="0.0.0.0", 
        port=getConfig().get("port"), 
        debug=True
    )
    
    
import os
import sys
import json
 
from flask import Flask, jsonify
from flask import request
from flask import Flask 
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


#===============================================================
# Global Variables Initialization
#===============================================================

app = Flask(__name__, static_folder='static', static_url_path='')
               
setUploadConfigs(app)
               
#################################################################

@app.route('/')
def index():
    return 'Services avialable'

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

@app.route('/create/<name>/<slug>/<active>/<spread_sheet_path>/<image_path>', methods=['GET', 'POST'])
def create(name, slug=None, active=True, spread_sheet_path=None, image_path=None):
    try:
    #     if request.method == 'POST':
    #         do_the_login()
    #     else:
    #         show_the_login_form()
                        
    #     ado.create();
                    
        active = active == 'True'            
        ProcessRequest().create(name, slug, active, spread_sheet_path, image_path)
        
        return returnSuccess();        

    except:
        return returnInternalError();        
        raise
        
#-----------------------------------------------------------------

@app.route('/update/<name>/<slug>/<active>/<spread_sheet_path>/<image_path>', methods=['GET'])
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

@app.route('/retrieve', methods=['GET'])
def retrieve():
    try:
        partners = ProcessRequest().readAll()        
        l = {"name": "aaaa", "slug": "bbb", "active": "True", "sheet": "?", "image": "?"}
        l2 = []
        l2.append(partners)
        return render_template('viewall.html', list=l2)

    except:
        return returnInternalError();        
        raise
        
#-----------------------------------------------------------------

@app.route('/upload', methods=['GET','POST'])
def upload():
    try:
        if request.method == 'POST':
            name = request.form['name']
            slug = request.form['slug']
            active = request.form['active']
    
            file = request.files['file']
            if file.filename:        
                if file and __allowedFile__(file.filename):
                    filename = secure_filename(file.filename)
                    
                    path = getFolderType(app, filename);
                    tmp = os.path.join(app.config['UPLOAD_FOLDER'], path)
                    if not os.path.isdir(tmp):
                        os.makedirs(tmp)
                        
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], path, filename))
                    
                    redir = path + "/" + filename
                    return redirect(url_for('viewUploadedFile', filename=redir))
        
            active = active.lower() == 'true'            
            spread_sheet_path = None
            image_path = None
            
            ProcessRequest().create(name, slug, active, spread_sheet_path, image_path)
        
            return redirect(url_for('index'))
        
        else:
            return render_template('upload.html')

    except:
        return returnInternalError();        
        raise

#-----------------------------------------------------------------
        
@app.route('/uploads/<path:filename>')
def viewUploadedFile(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    except:
        return returnInternalError();        
        raise
                            
#-----------------------------------------------------------------
                            
def __allowedFile__(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
            
#############################################################

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


#############################################################

if __name__ == '__main__':
    app.run(
        host="0.0.0.0", 
        port=getConfig().get("port"), 
        debug=True
    )
    
    
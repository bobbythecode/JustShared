import sys
import json
 
from flask import Flask, jsonify
from flask import request
from flask import Response
from flask import render_template

from handler import ProcessRequest
from ado import ADO 

from playhouse.shortcuts import model_to_dict, dict_to_model

from common.enums import *
from common.constants import *

from common.errors import *


#===============================================================
# Global Variables Initialization
#===============================================================

app = Flask(__name__, static_folder='static', static_url_path='')
dao = ADO(app);

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
                    
        ProcessRequest().create(name, slug, active, spread_sheet_path, image_path)
        return returnSuccess();        

    except:
        return returnInternalError();        
        raise
        
#-----------------------------------------------------------------

@app.route('/update/<name>/<slug>/<active>/<spread_sheet_path>/<image_path>', methods=['GET'])
def update(name, slug, active, spread_sheet_path, image_path):
    try:
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
        

#############################################################

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


#############################################################

if __name__ == '__main__':
    app.run(port=7000)
    
    
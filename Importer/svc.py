from flask import Flask
from flask import request
from flask import Response
from flask import render_template

import sys

from handler import ProcessRequest
from ado import ADO 

#################################################################

app = Flask(__name__)
dao = ADO(app);

#################################################################

@app.route('/')
def index():
    return 'Services avialable'

#-----------------------------------------------------------------

@app.route('/create/<name>/<slug>/<spread_sheet_path>/<image_path>', methods=['GET', 'POST'])
def create(name, slug=None, spread_sheet_path=None, image_path=None):
    try:
    #     if request.method == 'POST':
    #         do_the_login()
    #     else:
    #         show_the_login_form()
                        
    #     ado.create();
                    
        ProcessRequest().create()
        resp = Response('Error', status=503, mimetype='text/html')
        return resp;        

    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
        
    finally:
        return    

#-----------------------------------------------------------------

@app.route('/update/<name>/<slug>/<spread_sheet_path>/<image_path>', methods=['GET'])
def update(name, slug, spread_sheet_path, image_path):
    try:
        ProcessRequest().update()
        resp = Response('Error', status=503, mimetype='text/html')
        return resp;        

    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
        
    finally:
        return    

#-----------------------------------------------------------------

@app.route('/delete/<name>', methods=['GET'])
def delete(name):
    try:
        ProcessRequest().delete()
        resp = Response('Error', status=503, mimetype='text/html')
        return resp;        

    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
        
    finally:
        return    

#-----------------------------------------------------------------

@app.route('/read')
def read():
    try:
        ProcessRequest().read()
        resp = Response('Error', status=503, mimetype='text/html')
        return resp;        

    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
        
    finally:
        return    


#############################################################

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


#############################################################

if __name__ == '__main__':
    app.run(port=7000)
    
    
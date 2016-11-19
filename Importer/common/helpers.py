import os
from common.config import *

def getTypes(app):
    fs = getConfig().get("file_types")
    ts = json.loads(fs)
    typeSet = []
    for t in ts:
        typeSet.append(t["ext"])
        
    return typeSet   
                     
def assignTypes(app):
    app.config['ALLOWED_EXTENSIONS'] = getTypes(app)
    return    

def getFolderExt(app, filename):
    filename, ext = os.path.splitext(filename)
    ext = ext.replace(".", "")
    
    fs = getConfig().get("file_types")
    ts = json.loads(fs)
    for t in ts:        
        if ext == t["ext"]:
            return t["path"]
                        
    return ''    

def getFolderType(app, filename):
    filename, ext = os.path.splitext(filename)
    ext = ext.replace(".", "")
    
    fs = getConfig().get("file_types")
    ts = json.loads(fs)
    for t in ts:        
        if ext == t["ext"]:
            return t["type"]
                        
    return ''    

def setUploadConfigs(app):
    app.config['UPLOAD_FOLDER'] = getConfig().get("uploads")        
    
    # app.config['ALLOWED_EXTENSIONS'] = set(['csv', 'xls', 'png', 'jpg', 'jpeg'])
    assignTypes(app)
    
import os
from common.config import *
                     
def assignTypes(app):
    fs = getConfig().get("file_types")
    ts = json.loads(fs)
    typeSet = []
    for t in ts:
        typeSet.append(t["ext"])
        
    app.config['ALLOWED_EXTENSIONS'] = typeSet
    return    

def getFolderType(app, filename):
    filename, ext = os.path.splitext(filename)
    ext = ext.replace(".", "")
    
    fs = getConfig().get("file_types")
    ts = json.loads(fs)
    for t in ts:        
        if ext == t["ext"]:
            return t["path"]
                        
    return ''    

def setUploadConfigs(app):
    app.config['UPLOAD_FOLDER'] = getConfig().get("uploads")        
    
    # app.config['ALLOWED_EXTENSIONS'] = set(['csv', 'xls', 'png', 'jpg', 'jpeg'])
    assignTypes(app)
    
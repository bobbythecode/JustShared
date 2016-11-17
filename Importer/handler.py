import sys

class ProcessRequest():
    def __init__(self):
        return
    
    #-----------------------------------------------------------------
    
    def read(self):
        try:
            return "read"    
        
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
            
        finally:
            return    

    #-----------------------------------------------------------------
        
    def create(self):
        try:
            return "create"    
        
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
            
        finally:
            return    

    #-----------------------------------------------------------------

    def update(self):
        try:
            return "update"    
        
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
            
        finally:
            return    

    #-----------------------------------------------------------------

    def delete(self):
        try:
            return "delete"    
        
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
            
        finally:
            return    
        
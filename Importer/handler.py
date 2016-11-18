import sys
from model.entities.partnerEntity import *

class ProcessRequest():
    partner = PartnerRepo();
    
    def __init__(self): 
        return
    
    #-----------------------------------------------------------------
    
    def read(self, name):
        try:
            f = self.partner.read(name)            
            return f
         
        except:
            raise
             

    #-----------------------------------------------------------------
        
    def create(self, name, slug, active, spread_sheet_path, image_path):
        try:
            self.partner.insert(name, slug, active, spread_sheet_path, image_path)
        
        except:
            raise

    #-----------------------------------------------------------------

    def update(self, name, slug, active, spread_sheet_path, image_path):
        try:
            self.partner.update(name, slug, active, spread_sheet_path, image_path)
        
        except:
            raise
            
    #-----------------------------------------------------------------

    def delete(self, name):
        try:
            self.partner.delete(name)
            return
        
        except:
            raise
                    
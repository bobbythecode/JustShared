import sys
from model.entities.partnerEntity import *

class ProcessRequest():
    partner = PartnerRepo();
    
    def __init__(self): 
        return
    
    #-----------------------------------------------------------------
    
    def read(self, name):
        try:
            partner = self.partner.read(name)            
            return partner
         
        except:
            raise
             
    #-----------------------------------------------------------------
    
    def readAll(self):
        try:
            partners = self.partner.readAll()            
            return partners
         
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
                    
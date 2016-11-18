import json, sys

from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

from model.entities.base import BaseModel
from model.entities.base import getDb
from common.errors import *

class Partner(BaseModel):
    name = CharField(unique=True)
    slug = TextField(null=True)
    active = BooleanField(default=True, null=True)
    spread_sheet_path = TextField(null=True)
    img_path = TextField(null=True)


class PartnerRepo():
    def __init__(self):
        getDb().connect()
    
    #-------------------------------------------------------------------------------------
    
    def insert(self, name, slug, active, spread_sheet_path, image_path):
        try:
    #         e = Partner.get(Partner.name == name)         
    #         if e is not None:
    #             raise DuplicatedError("The partner name ", name, " duplicated")
    
            partner = Partner.create(name=name, slug=slug, spread_sheet_path=spread_sheet_path, image_path=image_path)
            partner.save()

        except IntegrityError as e:
            raise DuplicatedError("The partner name ", name, " duplicated")
                
    #-------------------------------------------------------------------------------------
    
    def update(self, name, slug, active, spread_sheet_path, image_path):
        try:
            partner = self.read(name);
            if partner is None:
                raise NotFoundError("The partner name ", name, " not found")
    
            partner.slug = 'bar'
            partner.active = active
            partner.spread_sheet_path = 'bar'
            partner.image_path = 'bar'

            partner.save()

        except:
            raise    

    #-------------------------------------------------------------------------------------
    
    def delete(self, name):
        try:
            partner = self.read(name);
            if partner is None:
                raise NotFoundError("The partner name ", name, " not found")
            
            partner.delete_instance()();
    #         e.save()
        except:
            raise    

    #-------------------------------------------------------------------------------------
    
    def read(self, name):
        try:
            partner = Partner.get(Partner.name == name)        
            return partner;
        
        except Exception as e:
            if type(e).__eq__("PartnerDoesNotExist"):
                raise NotFoundError("The partner name ", name, " not found")
            
            else: 
                raise    
            
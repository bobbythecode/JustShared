import os
import json
import unittest
import tempfile
import urllib2

from time import sleep
from flask import Flask

from svc import app
from model.entities.base import getDb
from model.entities.partnerEntity import *

class SvcTestCase(unittest.TestCase):

    def setUp(self):
        self.__clearDb__()
        getDb().connect();
        
    #-----
        
    def tearDown(self):
        if getDb().is_closed() == False:
            getDb().close()

    #-----
        
    def __clearDb__(self):    
        partner = Partner.delete().where(Partner.id > 0)
        partner.execute()

    #-----

    def __initDb__(self):    
        Partner.create(name='Albert')
        Partner.create(name='Bobby')
        Partner.create(name='Chalie')
        Partner.create(name='Duke')
                
    #-------------------------------------------------------------------------------
    
    def test_insertDb(self):
        albert = Partner.create(name='Albert')
        partner = Partner.get(Partner.name == 'Albert')
        
        self.assertEqual(partner.name, 'Albert')

    #-------------------------------------------------------------------------------
    
    def test_updateDb(self):
        albert = Partner.create(name='Albert')
        partner = Partner.get(Partner.name == 'Albert')
        
        self.assertEqual(partner.name, 'Albert')

        partner.name = 'Bobby'
        partner.save()
        
        partner = Partner.get(Partner.name == 'Bobby')
        self.assertEqual(partner.name, 'Bobby')

    #-------------------------------------------------------------------------------
    
    def test_deleteDb(self):
        albert = Partner.create(name='Albert')
        partner = Partner.get(Partner.name == 'Albert')
        
        self.assertEqual(partner.name, 'Albert')
        partner.delete_instance()
        
        partner = Partner.select().where(Partner.name == 'Albert')
        self.assertEqual(partner.exists(), False)
                    
    #-------------------------------------------------------------------------------
    
    def test_read(self):
        self.__initDb__()
        sleep(2)
        
        tester = app.test_client(self)
        response = tester.get('/read/Albert', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
        foo = json.loads(response.data);        
        self.assertEqual(foo["name"], "Albert")
 
    #-------------------------------------------------------------------------------
     
    def test_serviceCreate(self):
        name = 'Albert'
        slug = 'Foo'
        active = True
        spread_sheet_path = r"xxxx"
        img_path = r"cccc"
        
        argString = "/create/%s/%s/%s/%s/%s" % (name, slug, active, spread_sheet_path, img_path)
        
        tester = app.test_client(self)
        response = tester.get(argString, content_type='application/json')        
        self.assertEqual(response.status_code, 200)

        
        partner = Partner.select().where(
            Partner.name == name, 
            Partner.slug == slug,
            Partner.active == active,
            Partner.spread_sheet_path == spread_sheet_path,
            Partner.img_path == img_path)
                        
        self.assertEqual(partner.exists(), True)
                
    #-------------------------------------------------------------------------------

    def test_serviceUpdate(self):
        name = 'Albert'
        slug = 'Foo'
        active = True
        spread_sheet_path = r"xxxx"
        img_path = r"cccc"
                
        albert = Partner.create(
            name=name,
            slug=slug,
            active=active,
            spread_sheet_path=spread_sheet_path,
            img_path=img_path)
        
        partner = Partner.select().where(
            Partner.name == name, 
            Partner.slug == slug,
            Partner.active == active,
            Partner.spread_sheet_path == spread_sheet_path,
            Partner.img_path == img_path)
                        
        self.assertEqual(partner.exists(), True)

        slug2 = 'Foo2'
        active2 = False
        spread_sheet_path2 = r"yyyy"
        img_path2 = r"dddd"

        argString = "/update/%s/%s/%s/%s/%s" % (name, slug2, active2, spread_sheet_path2, img_path2)

        tester = app.test_client(self)
        response = tester.get(argString, content_type='application/json')        
        self.assertEqual(response.status_code, 200)
         
        partner2 = Partner.select().where(
            Partner.name == name, 
            Partner.slug == slug2,
            Partner.active == active2,
            Partner.spread_sheet_path == spread_sheet_path2,
            Partner.img_path == img_path2
        )
                                                    
        self.assertEqual(partner2.exists(), True)

    #-------------------------------------------------------------------------------

    def test_serviceDelete(self):
        name = 'Albert'
        slug = 'Foo'
        active = True
        spread_sheet_path = r"xxxx"
        img_path = r"cccc"
                
        Partner.create(
            name=name,
            slug=slug,
            active=active,
            spread_sheet_path=spread_sheet_path,
            img_path=img_path)
        
        partner = Partner.select().where(
            Partner.name == name, 
            Partner.slug == slug,
            Partner.active == active,
            Partner.spread_sheet_path == spread_sheet_path,
            Partner.img_path == img_path)
                        
        self.assertEqual(partner.exists(), True)
        
        argString = "/delete/%s" % (name)
        
        tester = app.test_client(self)
        response = tester.get(argString, content_type='application/json')        
        self.assertEqual(response.status_code, 200)

        
        partner = Partner.select().where(Partner.name == name) 
        self.assertEqual(partner.exists(), False)
        

if __name__ == '__main__':
    unittest.main()
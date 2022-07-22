import os

import certifi

import requests

import sys

import time

import json




class InventoryModule():

    NAME = 'bts.servicenow.cmdb_servers'

    def verify_file(self,path):

        pass

    def get_table(self,table,display_value = True):

       

        '''

        # UNCOMMENT THESE THREE LINES BEFORE DEPLOYING TO SERVER

        host = os.getenv("SN_HOST")

        username = os.getenv("SN_USERNAME")

        password = os.getenv("SN_PASSWORD")

        '''  

       

        url = "{}/api/now/table/{}".format(host,table)

        params = {'sysparm_display_value': display_value, 'sysparm_exclude_reference_link': 'true'}

       

   

        request= requests.get(url=url , params= params, auth= (username,password), verify= 'Inventory\\perm_chain.pem')

        if request.status_code == 200:

            parsed_dict = json.loads(request.json())

            return parsed_dict['result']

        else:

            return dict({None})
try1 = InventoryModule()

try1.get_table('cmdb_ci_app_server_websphere')

'''

Author : Sam McCoy

Description : Calls the ServiceNow API to get a list of servers

Imports: [

requests : Used to call the REST API and to GET from ServiceNow, passed in the url, username, and password.

sys : Used for error handling through redirecting error files and to replace the python print() functunality with a sys.stdout.write() which can be more reliable.

os : Allows for file handling and a number of other useful functionalities.

json : Allows for the parsing of the requests output into a json file so that it can be turned given to dynamic inventory to parse and prune.

]

'''

 

import requests
import sys
import os
import json

class callerAPI():
    def __init__(self):
        print(requests.certs.where())
        self.LOG_STATUS = "status_logfile"
        self.LOG_JSON = "jsonTest.json"
        if os.path.exists(self.LOG_STATUS):
            self.API_status_code = open(self.LOG_STATUS,"a")
        else:
            self.API_status_code = open(self.LOG_STATUS,"w")
        if os.path.exists(self.LOG_JSON):
            os.remove(self.LOG_JSON)
            self.parsedJSON = open(self.LOG_JSON,"w")
        else:
            self.parsedJSON = open(self.LOG_JSON,"w")
        self.restAPIcall = requests.get(url,auth=(username,password))
        self.status_code = self.restAPIcall.status_code
        if (self.status_code == 200):
            self.API_status_code.write('SUCCESS;200\n')
            self.parsed_dict = json.loads(self.restAPIcall.text)
            self.parsed_json = json.dumps(self.parsed_dict,indent= 4)
            self.parsedJSON.write(self.parsed_json)
        else:
            self.API_status_code.write('FAILURE:'+str(self.status_code)+"\n")
            sys.stdout.write("failure")

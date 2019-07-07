import json
import os 

with open("./ng_exceptions/error.json",'r') as fs:
        data = fs.read()
        errors = json.loads(data)
        

def trans(formatted):
        for i in errors:
                err = i['from']
                if err in formatted:
                        formatted+=i['to']
        return formatted


    
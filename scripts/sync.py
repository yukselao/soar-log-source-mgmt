#!/usr/bin/env python

import logging
import requests
import urllib3
import json
import sys
import traceback
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



token='adbe9156-4532-4830-9442-a014938d112e'
server='https://10.10.2.10/api'

header={}
header['SEC'] = token
header['Version']= "16.0"
header['Accept'] = "application/json"
header["Content-Type"]= "application/json"

excludelist=[18]

url='/config/event_sources/log_source_management/log_source_types'
serverurl=server+url
req=requests.get(serverurl,headers=header,verify=False)
types=req.json()
def gettypename(mytype):
    global types
    mtype=str(mytype)
    for tdata in types:
        if str(tdata['id'])==str(mytype):
            return tdata['name']


url='/config/event_sources/log_source_management/log_source_groups'
serverurl=server+url
req=requests.get(serverurl,headers=header,verify=False)
groups=req.json()
def getgroupname(mygroup):
    global groups
    mygroup=str(mygroup)
    for tdata in groups:
        if str(tdata['id'])==str(mygroup):
            return tdata['name']


def main():
	try:
		url='/config/event_sources/log_source_management/log_sources'
		serverurl=server+url
		req=requests.get(serverurl,headers=header,verify=False)
		result=req.text.encode('utf-8')
		out=[]
		for data in req.json():
		    if data['type_id'] not in excludelist:
		        url='/config/event_sources/log_source_management/log_sources/'+str(data['id'])+'?fields=group_ids'
		        serverurl=server+url
		        req2=requests.get(serverurl,headers=header,verify=False)
		        data2=req2.json()
		        groups=[]
		        for groupid in data2['group_ids']:
		                groups.append(getgroupname(groupid))
		        data["groups"]=groups
		        data["lstype"]=gettypename(data['type_id'])
		    out.append(data)
		f=open("out.json","w")
		f.write(json.dumps(out))
		f.close()
		sys.exit(0)
	except Exception as e:
		print(traceback.format_exc())
		sys.exit(1)


if __name__ == '__main__':
	main()
#print(data['name']+' - Status:'+data['status']['status'])
#print(str(data['type_id'])+' - '+gettypename(data['type_id']))

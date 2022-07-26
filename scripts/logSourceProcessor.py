#!/usr/bin/env python



import sys, traceback, json, datetime, os, requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

jsondir="./jsondata/"


def search(name):
	payload='{"filters":[{"conditions":[{"field_name":"incident_type_ids","method":"in","value":[1015,1011,1014,1013,1012]},{"field_name":"name","method":"contains","value":"%s"}]}],"sorts":[],"start":0,"length":10}' % name
	header={}
	header["Content-Type"]= "application/json"
	session = requests.Session()
	session.auth = ("8a96e5e5-4c19-471b-8e9c-39d5c0004e8d","65diYOertVzsYmsLXhUlrC0zugptJ2QJ0TmEc7JpcBs")
	url='https://10.10.2.50/rest/orgs/201/incidents/query_paged?return_level=full&field_handle='
	req=session.post(url,headers=header,data=payload,verify=False)
	if req.json()["recordsTotal"]>0:
		return req.json()["recordsTotal"], req.json()["data"][0]["id"]
	else:
		return req.json()["recordsTotal"], 0

def main():
	logfile=sys.argv[1]
	if os.path.isfile(logfile):
		f=open(logfile,"r")
		data=''.join(f.readlines())
		f.close()
		jsondata=json.loads(data)
		for ls in jsondata:
			status=ls["status"]["status"].lower()
			name=str(ls["id"])+"# " +ls["name"]
			recordsTotal, incidentid=search(name)
			if recordsTotal==0:
				filename=jsondir+"create-"+str(ls["id"])+".json"
			else:
				filename=jsondir+"update-"+str(incidentid)+".json"
			incidentData={}
			incidentData["name"]=name
			incidentData["status"]=status
			incidentData["description"]=ls["description"]
			if "last_event_time" in ls and ls["last_event_time"]!=0:
				ts=ls["last_event_time"]
				ts=int(str(ts)[0:-3])
			incidentData["properties"]={}
			incidentData["properties"]["qradar_log_source_name"]=ls["name"]
			incidentData["properties"]["qradar_log_source_id"]=str(ls["id"])
			incidentData["properties"]["qradar_log_source_status"]=str(status)
			incidentData["properties"]["qradar_log_source_last_control_time"]=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			if "lstype" in ls:
				incidentData["properties"]["qradar_log_source_type"]=ls["lstype"]
			incidentData["properties"]["qradar_log_source_last_event_ts"]=str(ts)
			incidentData["properties"]["qradar_log_source_last_event_time"]=datetime.datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
			if status=="disabled":
				incidentTypeId=1015
			elif status=="error":
				incidentTypeId=1011
			elif status=="na":
				incidentTypeId=1014
			elif status=="success":
				incidentTypeId=1013
			elif status=="warning":
				incidentTypeId=1012	
			incidentData["incident_type_ids"]=[int(incidentTypeId)]
			jsonstr=json.dumps(incidentData, indent=4, sort_keys=True)
			f=open(filename,"w")
			f.write(jsonstr)
			f.close()
				
	else:
		print(logfile+" not found")

if __name__=="__main__":
	main()

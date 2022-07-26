#!/bin/bash



#{"name":"Default name","description":"Default description","incident_type_ids":[1013]}

source common.sh

curl -k -X POST -u $(getconf authconfig) -H "Content-Type: application/json" -d '{"name":"Default name1111","description":"Default description","incident_type_ids":[1013],"discovered_date": 1649852577300}' 'https://10.10.2.50/rest/orgs/201/incidents'

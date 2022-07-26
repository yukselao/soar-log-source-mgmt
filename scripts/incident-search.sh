#!/bin/bash

source common.sh

curl -k -X POST -u $(getconf authconfig) -H "Content-Type: application/json" -d '{"filters":[{"conditions":[{"field_name":"incident_type_ids","method":"in","value":[1015,1011,1014,1013,1012]},{"field_name":"name","method":"contains","value":"Log Source 123"}]}],"sorts":[],"start":0,"length":10}' 'https://10.10.2.50/rest/orgs/201/incidents/query_paged?return_level=full&field_handle='

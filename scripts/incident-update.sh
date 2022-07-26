#!/bin/bash



#{"name":"Default name","description":"Default description","incident_type_ids":[1013]}

source common.sh

# method 1:
#curl -k -X PATCH -u $(getconf authconfig) -H "Content-Type: application/json" -d '{"changes":[{"field":"incident_type_ids","old_value":{"ids":[1015]},"new_value":{"ids":[1012]}}]}' 'https://10.10.2.50/rest/orgs/201/incidents/2126'



echo '{"incident_type_ids":[1013]}' > incident-update.json
gadget --update /incidents/2126 incident-update.json

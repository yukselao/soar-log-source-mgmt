#!/bin/bash

source common.sh

time curl -k -X DELETE -u $(getconf authconfig) -H "Content-Type: application/json" 'https://10.10.2.50/rest/orgs/201/incidents/2306/table_data/ldap_query_results/row_data'

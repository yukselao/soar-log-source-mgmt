#!/bin/bash

source common.sh

curl -s -k -u $(getconf authconfig) -H "Content-Type: application/json" 'https://10.10.2.50/rest/orgs/201/incidents/2095/workflow_instances'

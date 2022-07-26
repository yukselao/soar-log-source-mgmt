#!/bin/bash

cd /home/appadmin/ibm

source init.sh
source scripts/myenv
source scripts/common.sh

function plog() {
	echo $(date "+%F %T") $@
}

plog INFO "started"

cd scripts/
./sync.py
if [ $? -eq 0 ]; then
	/bin/rm -fr jsondata/
	mkdir -p jsondata/
	./logSourceProcessor.py out.json
	cd jsondata/
	ls -1 create* 2>/dev/null |while read line; do
		gadget --create $line &>/dev/null
		if [ $? -eq 0 ]; then
			plog INFO gadget --create $line
		else
			plog ERROR gadget --create $line
		fi
	done
	ls -1 update* 2>/dev/null |while read line; do
		incidentid="$(echo $line |awk -F'-' '{print $2}' |sed -r 's#.json##')"
		gadget --update /incidents/${incidentid}  $line &>/dev/null
		if [ $? -eq 0 ]; then
			plog INFO gadget --update /incidents/${incidentid}  $line
		else
			plog ERROR gadget --update /incidents/${incidentid}  $line
		fi
	done
else
	echo "Notify admin"
fi

plog INFO "completed"

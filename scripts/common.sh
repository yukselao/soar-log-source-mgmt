

homefolder=/home/appadmin/ibm/
function getconf() {
	cat $homefolder/config.ini |egrep "^$1=" |awk -F'=' '{ print $2 }'
}

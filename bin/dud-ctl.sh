#!/bin/bash
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi
dud_reset(){
	PIDFILE=/var/lock/dud.pid
	if [ -f $PIDFILE ] ; then
		kill `cat $PIDFILE`
		rm $PIDFILE
	fi
	/usr/local/bin/dud.py 0
}


dud_xmin(){
	dud_reset
	PIDFILE=/var/lock/dud.pid
	echo $$ > $PIDFILE
	/usr/local/bin/dud.py 1
	sleep $(( 60 * $1 ))
	/usr/local/bin/dud/py 0
	rm $PIDFILE
}

case $1 in 
	reset)
		dud_reset
	;;
	xmin)
		dud_xmin $2
	;;
	*)
		exit 3
	;;
esac



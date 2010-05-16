#
# Regular cron jobs for the easyzone package
#
0 4	* * *	root	[ -x /usr/bin/easyzone_maintenance ] && /usr/bin/easyzone_maintenance

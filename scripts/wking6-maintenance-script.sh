#!/usr/bin/env bash
#This script is to AUTOMATE the maintenance process for the user 'wking6'
#
#For individual TAs and Instructors, please feel free to modify this script to your own liking as long as it is in
#compliance with the Technical Document policies
#
#For any configuration changes, please refer to the Technical Documentation in Section 15.3
#
#Last Revision: May 16th, 2017 5:33 PM/EST
#
#
#Script merged into Maintenance.py on May 16th, this file stands as an example of how to create a custom automated Maintenance script

DATE=`date +%m%d%Y`
tar -czvf edx_logs_backup_$DATE.tar.gz /edx/var/log
tar -czvf logs_backup_$DATE.tar.gz /var/log
mv edx_logs_backup_$DATE.tar.gz /gt/backup/logs
mv logs_backup_$DATE.tar.gz /gt/backup/logs
cp logs_backup_$DATE.tar.gz /home/wking6
cp edx_logs_backup_$DATE.tar.gz /home/wking6
chown wking6 /home/wking6/*
/gt/manage.py do manage_script_upgrade
/gt/manage.py do backup
/gt/manage.py do system_upgrades
echo Do not forget to copy the DB Backups and reboot the machine
echo Once the machine reboots, run /gt/manage.py do refresh firewall_rules


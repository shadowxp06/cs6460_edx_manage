#!/usr/bin/python
#
# This file relates around commands related to Maintenance, including running custom maintenance scripts
#
# Last Updated: 05/20/2017 3:18 PM/EST
#

import Constants
import MiscUtils
import shell_functions
import os
import shutil


class Maintenance(object):
    __user__ = ""
    __hasMaintenanceStarted__ = False

    def __init__(self, user):
        self.__user__ = user
        self.__hasMaintenanceStarted__ = False

    def __init__(self):
        self.__user__ = "root"
        self.__hasMaintenanceStarted__ = False

    def start_maintenance(self):
        if self.__hasMaintenanceStarted__ is False:
            MiscUtils.write_to_log(Constants.maintenance_log, MiscUtils.get_current_user() + " has started Maintenance") #TODO: Create Constant
            os.system("sudo service nginx stop")
            self.__hasMaintenanceStarted__ = True

    def end_maintenance(self):
        if self.__hasMaintenanceStarted__ is True:
            MiscUtils.write_to_log(Constants.maintenance_log, MiscUtils.get_current_user() + " has ended Maintenance") #TODO: Create Constant
            os.system("sudo service nginx start")
            self.__hasMaintenanceStarted__ = False

    def run_maintenance_script(self,user): #Use only if you do something special with Maintenance (though you shouldn't need to!)
        MiscUtils.write_to_log(Constants.mgmt_system_log, MiscUtils.get_current_user() + " is running User Maintenance script : " + user) #TODO: Create Constant
        su = shell_functions.Shell_Script(shell_functions.get_script_dir(), user + "-maintenance-script.sh")
        su.run_script()

    def run_db_backup(self):
        print(Constants.header + " " + Constants.backup_log)
        if self.__hasMaintenanceStarted__ is True:
            if MiscUtils.check_for_backup_dir():
                cur_logtime = MiscUtils.get_logtime_format()
                os.system("mongodump -h 127.0.0.1:" + Constants.mongodb_port + " -o " + MiscUtils.get_backup_dir() + cur_logtime + "_mongo-backup")
                os.system("mongodump -h 127.0.0.1:" + Constants.mongodb_port + " -o " + Constants.edx_backup_loc)
                os.system("mysqldump -u " + Constants.mysql_db_backup_user + " -p --all-databases > " + MiscUtils.get_backup_dir() + cur_logtime + "_mongo-backup/" + cur_logtime + "_mysql-backup.sql")
                shutil.make_archive(cur_logtime, "zip", MiscUtils.get_backup_dir() + cur_logtime + "_mongo-backup")
                os.system("sudo rm -rf " + MiscUtils.get_backup_dir() + cur_logtime + "_mongo-backup")
                os.system("sudo cp " + cur_logtime + ".zip " + MiscUtils.get_backup_dir() + "db/")
                os.system("sudo rm " + cur_logtime + ".zip")
                print(Constants.header + " " + Constants.backup_log_complete + MiscUtils.get_backup_dir())
        else:
            print(Constants.maintenance_error)

    def run_management_script_update(self):
        print(Constants.header + " " + Constants.management_script_upgrade)
        os.system("git config --global credential.helper \"cache --timeout=3600\"")
        os.system("cd " + MiscUtils.get_python_dir() + " && sudo git reset --hard HEAD")
        os.system("cd " + MiscUtils.get_python_dir() + " && sudo git clean -f")
        os.system("cd " + MiscUtils.get_python_dir() + " && sudo git pull")
        print(Constants.header + Constants.done)
        MiscUtils.write_to_log(Constants.mgmt_system_log,
                               MiscUtils.get_current_user() + " " + Constants.management_script_upgrade_log)

    def run_edx_logs_backup(self):
        print(Constants.header + " " + Constants.open_edx_logs_backup)
        cur_logtime = MiscUtils.get_logtime_format()
        shutil.make_archive("edx_logs_backup_" + cur_logtime, "zip", Constants.edx_logs_loc)
        os.system("mv edx_logs_backup_" + cur_logtime + ".zip " + MiscUtils.get_backup_dir() + "logs/")
        MiscUtils.write_to_log(Constants.mgmt_system_log, MiscUtils.get_current_user() + " " + Constants.open_edx_logs_backup_log)


    def run_logs_backup(self):
        print(Constants.header + " " + Constants.logs_backup)
        cur_logtime = MiscUtils.get_logtime_format()
        shutil.make_archive("logs_backup_" + cur_logtime, "zip", Constants.logs_loc)
        os.system("mv logs_backup_" + cur_logtime + ".zip " + MiscUtils.get_backup_dir() + "logs/")
        MiscUtils.write_to_log(Constants.mgmt_system_log, MiscUtils.get_current_user() + " " + Constants.logs_loc)


    def run_normal_maintenance(self):
        print(Constants.header + " " + Constants.maintenance_start)
        self.start_maintenance()
        self.run_edx_logs_backup()
        self.run_logs_backup()
        self.run_management_script_update()
        self.run_db_backup()
        su = shell_functions.System_Updates(True, True)  # Mark the package and run upgrades
        su.run_all()
        self.end_maintenance()
        print(Constants.header + " " + Constants.maintenance_end_warn1) #TODO: Convert this into a String Array and iterate through
        print(Constants.header + " " + Constants.maintenance_end_warn2) #TODO: Convert this into a String Array and iterate through
        print(Constants.header + " " + Constants.maintenance_end)

    def run_system_upgrades(self):
        su = shell_functions.System_Updates(True, True)  # Mark the package and run upgrades
        su.run_all()
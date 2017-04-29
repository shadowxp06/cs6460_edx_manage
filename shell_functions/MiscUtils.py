#
# Last Updated: 04/15/2017 9:39 PM/EST
#

import os
import Constants
import errno
import getpass
from time import gmtime, strftime
import shutil
import MiscUtils
import subprocess
import string
import Supervisor
from validate_email import validate_email


def do_backup():
    print(Constants.header + " " + Constants.backup_log)
    if check_for_backup_dir():
        cur_logtime = get_logtime_format()
        os.system("mongodump -h 127.0.0.1:" + Constants.mongodb_port + " -o " + get_backup_dir() + cur_logtime + "_mongo-backup")
        os.system("mongodump -h 127.0.0.1:" + Constants.mongodb_port + " -o " + Constants.edx_backup_loc)
        os.system("mysqldump -u " + Constants.mysql_db_backup_user + " -p --all-databases > " + get_backup_dir() + cur_logtime + "_mongo-backup/" + cur_logtime + "_mysql-backup.sql")
        shutil.make_archive(get_logtime_format(), "zip", get_backup_dir() + cur_logtime + "_mongo-backup")
        os.system("rm -rf " + get_backup_dir() + cur_logtime + "_mongo-backup")
    print(Constants.header + " " + Constants.backup_log_complete + get_backup_dir())


def do_management_script_update():
    print(Constants.header + " " + Constants.management_script_upgrade)
    os.system("git config --global credential.helper \"cache --timeout=3600\"")
    os.system("cd " + get_python_dir() + " && sudo git reset --hard HEAD")
    os.system("cd " + get_python_dir() + " && sudo git clean -f")
    os.system("cd " + get_python_dir() + " && sudo git pull")
    print(Constants.header + Constants.done)
    MiscUtils.write_to_log(Constants.mgmt_system_log,
                           MiscUtils.get_current_user() + " " + Constants.management_script_upgrade_log)


#TODO: Move this into it's own Course command
def do_list_course_ids():
    print(Constants.header + Constants.openedx_list_course_ids)
    os.system("cd /edx/app/edxapp/edx-platform && sudo -u www-data /edx/bin/python.edxapp /edx/bin/manage.edxapp lms dump_course_ids --settings aws")
    print(Constants.header + Constants.done)


#TODO: Move this into it's own Course command
def do_delete_course(courseid):
    print(Constants.header + Constants.openedx_remove_course)
    print(Constants.openedx_backup_nag)
    os.system("sudo -u www-data /edx/bin/python.edxapp /edx/bin/manage.edxapp cms delete_course " + courseid + " --settings aws")
    print(Constants.done)


#TODO: Move this into it's own Base command
#TODO: Add support for CMS
def do_lms_asset_recompile():
    print(Constants.header + Constants.openedx_compile_assets)
    os.system("cd /edx/app/edxapp/edx-platform && paver update_assets lms --settings=aws")
    sv = Supervisor.Supervisor("restart")
    sv.cmd = sv.cmd + " edxapp:"
    sv.run()
    print(Constants.header + Constants.done)
    MiscUtils.write_to_log(Constants.mgmt_system_log, MiscUtils.get_current_user() + " " + Constants.openedx_compile_assets_lms_log)


def do_netstat():
    print(Constants.header + " " + Constants.netstat)
    os.system("netstat -anltp | grep LISTEN")
    print(Constants.header + Constants.done)


def get_current_dir():
    return os.getcwd()


def get_python_dir():
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_script_dir():
    return get_python_dir() + "/scripts/"


def get_backup_dir():
    return get_python_dir() + "/backup/"


def get_config_dir():
    return get_python_dir() + "/config/"


def get_log_dir():
    return get_python_dir() + "/logs/"


def check_for_backup_dir(): #See http://stackoverflow.com/questions/273192/how-to-check-if-a-directory-exists-and-create-it-if-necessary for this particular bit of code
    if os.path.exists(get_backup_dir()):
        return True
    else:
        try:
            os.makedirs(get_backup_dir())
            return check_for_backup_dir()  # This may fail if the user is not root when running backup
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise


def check_for_log_dir():
    if os.path.exists(get_log_dir()):
        return True
    else:
        try:
            os.makedirs(get_log_dir())
            return check_for_log_dir()  # This may fail if the user is not root when running backup
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise


def get_logtime_format(): #See http://stackoverflow.com/questions/415511/how-to-get-current-time-in-python for this particular bit of code
    return strftime("%m%d%Y_%H%M%S", gmtime())


def get_syslog_format():
    return strftime("%m-%d-%Y %H:%M:%S", gmtime())


def write_to_log(log_file, line):
    if check_for_log_dir(): #TODO: Add checking to see if the log file exists
        myFile = open(get_log_dir() + log_file, 'a')
        myFile.write("(" + get_syslog_format() + ") " + line)
        myFile.write("\n")
        myFile.close()


def get_current_user():
    return getpass.getuser()


def delete_file(file):
    if os.path.isfile(file):
        os.system("sudo rm -rf " + file)
    else:
        print(Constants.delete_file_error + " " + file)


# See http://stackoverflow.com/questions/13104944/how-to-find-out-with-python-on-ubuntu-if-mysql-is-running
def check_for_process(processname):
    msqlr = subprocess.Popen("sudo /bin/netstat -al".split(), stdout=subprocess.PIPE).stdout
    grep = subprocess.Popen(["/bin/grep", processname], stdin=msqlr, stdout=subprocess.PIPE).stdout
    msqlrLines = grep.read().split("\n")
    vals = map(string.strip, msqlrLines[0].split())
    vals_length = len(vals)
    i = 0
    isRunning = False
    while i < vals_length:
        if vals[i] == "LISTENING" or vals[i] == "LISTEN":
            isRunning = True
        i += 1

    return isRunning


#See http://stackoverflow.com/questions/8022530/python-check-for-valid-email-address
def isValidEmail(userEmail):
    return  validate_email(userEmail)
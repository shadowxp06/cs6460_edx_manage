#
# Last Updated: 04/21/2017 10:17 PM/EST
#
header = "(CS6460 Open EdX) "
edx_backup_loc = "/edx/backup/"
mongodb_port = "45172"
mysql_db_backup_user = "root"

# Logging Constants
mgmt_system_log = "system.log"
help_csv = "help.csv"
msg_for_more_help = "For more help, try manage.py help <command>"
not_implemented_message = "Command or option not implemented"

# Config dir names
denyhosts = "denyhosts"
mongo = "mongo"
mysql = "mysql"
nginx = "nginx"
openedx = "openedx"
ssh = "ssh"

# Messages

# Generic
done = "Done"
delete_file_error = "Cannot find file to delete:"
restart = "Restart"
restart_log = "has restarted service :"
experimental = "This feature or command is currently marked as Experimental, \n if you still wish to run it, add _experimental to the command that you are trying to run"
script_not_found = "Script not found -- it is recommended that you do a git fetch --all"
command_not_found = "Command not found -- use -help for more information"
option_not_found = "Option not found or supported"

# OpenEdX
begin_openedx_upgrade = "Beginning Open EdX Upgrade"
end_openedx_ugprade = "Open EdX Upgrade Done - Please check the GT Technical Documentation for after upgrade notes"
upgrade_openedx_log_message = "has run Do OpenEdX_Upgrade_Experimental"
openedx_upgrade_stg1 = "Beginning Open EdX Upgrade - Stage 1"
openedx_upgrade_stg1_complete = "Open EdX Upgrade - Stage 1 - Complete"
openedx_upgrade_stg2 = "Beginning Open EdX Upgrade - Stage 2"
openedx_upgrade_stg2_complete = "Open EdX Upgrade - Stage 2 - Complete"
openedx_remove_json = "Removing JSON Files that the OpenEdX Upgrader copied"
openedx_remove_nginx = "Remove old Nginx files"
openedx_list_course_ids = "List of Course IDs"
openedx_remove_course = "Remove course"
openedx_backup_nag = "Make sure you run manage.py do backup before running this command"
openedx_compile_assets = "Compiling Assets"
openedx_compile_assets_lms_log = "has re-compiled the LMS Assets"
openedx_user_add_invalidemail = "Invalid Email Provided"
openedx_run_playbook = " has run the playbook: "

#System_Updates
system_updates_mark_package = "Marking Packages for Hold"
system_updates_mark_package_log = "has run Mark Packages successfully"
system_updates_mark_package_log_unsuccessful = "has run Mark Packages unsuccessfully"
system_updates_run_upgrades = "Running Upgrades"
system_updates_run_upgrades_successful = "has run Run Upgrades Successfully"
system_updates_run_upgrades_unsuccessful = "has run Run Upgrades Successfully"

#Refresh
refresh_log = "has run do refresh"
refresh_openedx = "Refreshing OpenEdX Configuration"

#Search
begin_search = "Beginning search"
end_search = "End of search"

#Backup
backup_log = "Running database backup"
backup_log_complete = "Backup is done - you can find it in: "

#Manage.py
management_script_upgrade = "Starting Update for Manage.py"
management_script_upgrade_log = "has run Management Script Upgrade"

#Netstat
netstat = "Netstat -anltp"

#MySQL
change_user_pass = "has changed the MySQL User Pass for :"

#Shell_Script
execute_shell_script = "has executed script :"

#Supervisor
supervisor_log = "has run the supervisor command :"

#User
add_edx_user = "Adding a EdX Superuser"
add_edx_user_log = "has added a new superuser to EdX :"


#Check_Process
def process_is_running(procname, is_running):
    if is_running:
        print("The process " + procname + " is running")
    else:
        print("The process " + procname + " is not running")

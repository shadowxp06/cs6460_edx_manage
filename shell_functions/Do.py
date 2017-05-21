#!/usr/bin/python
#
# Last Updated: 05/16/2017 8:55 PM/EST
#
import Constants
import shell_functions
import os
import MiscUtils


class Do(object):
    def __init__(self):
        self.command = ""
        self.args = []
        self.totalArgs = len(self.args)
        self.release = ""

    def __init__(self, command):
        self.command = str(command).lower()
        self.args = []
        self.totalArgs = len(self.args)
        self.release = ""

    def __init__(self, command, args):
        self.command = str(command).lower()
        self.args = args #This should ALWAYS be an Array
        self.totalArgs = len(self.args)
        self.release = ""

    def do_command(self):
        self.totalArgs = len(self.args)
        if self.command == 'openedx_upgrade':
            print(Constants.experimental)
        elif self.command == 'openedx_upgrade_experimental':
            if self.totalArgs > 2:
                self.release = self.args[3]
                print(Constants.header + Constants.begin_openedx_upgrade)
                self.openedx_upgrade_stage1()
                self.openedx_upgrade_stage2()
                print(Constants.header + Constants.end_openedx_ugprade)
                MiscUtils.write_to_log(Constants.mgmt_system_log,
                                       MiscUtils.get_current_user() + " " + Constants.upgrade_openedx_log_message)
            else:
                print(Constants.option_not_found)
        elif self.command == 'manage_script_upgrade':
            su = shell_functions.Maintenance()
            su.run_management_script_update()
        elif self.command == 'service_status':
            sv = shell_functions.Supervisor.Supervisor("status")
            print(sv.run())
        elif self.command == 'refresh':
            if self.totalArgs > 3:
                self.refresh_command()
                MiscUtils.write_to_log(Constants.mgmt_system_log,
                                       MiscUtils.get_current_user() + " " + Constants.refresh_log + " " + self.args[3])
            else:
                print(Constants.option_not_found)
        elif self.command == 'show_netstat_listening':
            shell_functions.do_netstat()
        elif self.command == 'search_playbook':
            if self.totalArgs > 2:
                self.searchTerm = self.args[3]
                print(Constants.header + " " + Constants.begin_search)
                print(self.grep_search())
                print(Constants.header + " " + Constants.end_search)
        elif self.command == 'list_course_ids':
            if self.totalArgs > 2:
                MiscUtils.do_list_course_ids()
        elif self.command == 'lms_asset_compile':
            MiscUtils.do_lms_asset_recompile() #TODO: Fix for GT VM
        elif self.command == 'maintenance':
            if self.totalArgs > 3:
                self.maintenance_command()
                MiscUtils.write_to_log(Constants.mgmt_system_log, MiscUtils.get_current_user() + " has run the maintenance command: " + self.args[3])
        else:
            print(Constants.command_not_found)


    def maintenance_command(self):
        su = shell_functions.Maintenance()
        if self.args[3] == 'backup':
            su.run_db_backup()
        elif self.args[3] == 'start':
            print(Constants.header + " " + Constants.maintenance_start)
            su.start_maintenance()
        elif self.args[3] == 'end':
            print(Constants.header + " " + Constants.maintenance_end)
            su.end_maintenance()
        elif self.args[3] == 'run':
            su.run_normal_maintenance()
        elif self.args[3] == 'db_backup':
            su.run_db_backup()
        elif self.args[3] == 'logs_backup':
            su.run_edx_logs_backup()
            su.run_logs_backup()
        elif self.args[3] == 'system_upgrades':
            su.run_system_upgrades()
        else:
            print(Constants.command_not_found)

    def refresh_command(self):
        if self.args[3] == 'firewall_rules':
            print(Constants.header + " " + Constants.refresh_firewall_rules)
            su = shell_functions.Shell_Script(shell_functions.get_script_dir(), "firewall_rules.sh")
            su.run_script()
            print(Constants.header + " " + Constants.done)
        elif self.args[3] == 'openedx_config':
            print(Constants.header + " " + Constants.refresh_openedx)
            self.openedx_upgrade_stage2(self, 'false')
            print(Constants.header + " " + Constants.done)
            MiscUtils.write_to_log(Constants.mgmt_system_log, MiscUtils.get_current_user() + " has refreshed the Open EdX Configuration")
        else:
            print(Constants.option_not_found)

    def openedx_upgrade_stage1(self):
        print(Constants.header + " " + Constants.openedx_upgrade_stg1)
        os.system("sudo /edx/bin/update edx-platform " + self.release)
        os.system("sudo /edx/bin/update edx-workers " + self.release)
        os.system("sudo /edx/bin/update xqueue " + self.release)
        os.system("sudo /edx/bin/update cs_comments_service " + self.release)
        os.system("sudo /edx/bin/update credentials " + self.release)
        os.system("sudo /edx/bin/update xserver " + self.release)
        os.system("sudo /edx/bin/update configuration " + self.release)
        os.system("sudo /edx/bin/update read-only-certificate-code " + self.release)
        os.system("sudo /edx/bin/update edx-analytics-data-api " + self.release)
        #os.system("sudo /edx/bin/update edx-ora2 " + self.release)
        #os.system("sudo /edx/bin/update insights " + self.release)
        os.system("sudo /edx/bin/update ecommerce " + self.release)
        os.system("sudo /edx/bin/update course_discovery " + self.release)
        os.system("sudo /edx/bin/update notifier " + self.release)
        print(Constants.header + " " + Constants.openedx_upgrade_stg1_complete)

    def openedx_upgrade_stage2(self,show_header='true'):
        if show_header == 'true':
            print(Constants.header + " " + Constants.openedx_upgrade_stg2)

        self.remove_old_json_files()
        self.remove_old_nginx_files()
        svc = shell_functions.Service_Restart("openedx")
        svc.restart_service()
        print(Constants.header + " " + Constants.openedx_upgrade_stg2_complete)

    def remove_old_json_files(self):
        print(Constants.header + " " + Constants.openedx_remove_json)
        shell_functions.delete_file("/edx/app/edxapp/cms.auth.json")
        shell_functions.delete_file("/edx/app/edxapp/cms.env.json")
        shell_functions.delete_file("/edx/app/edxapp/lms.auth.json")
        shell_functions.delete_file("/edx/app/edxapp/lms.env.json")
        os.system("sudo cp " + shell_functions.get_config_dir() + "openedx/cms.auth.json /edx/app/edxapp/")
        os.system("sudo cp " + shell_functions.get_config_dir() + "openedx/cms.env.json /edx/app/edxapp/")
        os.system("sudo cp " + shell_functions.get_config_dir() + "openedx/lms.auth.json /edx/app/edxapp/")
        os.system("sudo cp " + shell_functions.get_config_dir() + "openedx/lms.env.json /edx/app/edxapp/")
        print(Constants.header + " " + Constants.done)

    def remove_old_nginx_files(self):
        print(Constants.header + " " + Constants.openedx_remove_nginx)
        shell_functions.delete_file("/edx/app/nginx/sites-available/certs")
        shell_functions.delete_file("/edx/app/nginx/sites-available/cms")
        shell_functions.delete_file("/edx/app/nginx/sites-available/credentials")
        shell_functions.delete_file("/edx/app/nginx/sites-available/ecommerce")
        shell_functions.delete_file("/edx/app/nginx/sites-available/edx-release")
        shell_functions.delete_file("/edx/app/nginx/sites-available/forum")
        shell_functions.delete_file("/edx/app/nginx/sites-available/lms")
        shell_functions.delete_file("/edx/app/nginx/sites-available/xqueue")
        shell_functions.delete_file("/edx/app/nginx/sites-available/xserver")
        os.system("sudo cp " + shell_functions.get_config_dir() + "nginx/certs /edx/app/nginx/sites-available/")
        os.system("sudo cp " + shell_functions.get_config_dir() + "nginx/cms /edx/app/nginx/sites-available/")
        os.system("sudo cp " + shell_functions.get_config_dir() + "nginx/credentials /edx/app/nginx/sites-available/")
        os.system("sudo cp " + shell_functions.get_config_dir() + "nginx/ecommerce /edx/app/nginx/sites-available/")
        os.system("sudo cp " + shell_functions.get_config_dir() + "nginx/edx-release /edx/app/nginx/sites-available/")
        os.system("sudo cp " + shell_functions.get_config_dir() + "nginx/forum /edx/app/nginx/sites-available/")
        os.system("sudo cp " + shell_functions.get_config_dir() + "nginx/lms /edx/app/nginx/sites-available/")
        os.system("sudo cp " + shell_functions.get_config_dir() + "nginx/xserver /edx/app/nginx/sites-available/")
        os.system("sudo cp " + shell_functions.get_config_dir() + "nginx/xqueue /edx/app/nginx/sites-available/")
        print(Constants.header + " " + Constants.done)

    def grep_search(self):
        os.system("sudo  grep -rnw '/edx/app/edx_ansible/edx_ansible/playbooks/' -e \"" + self.searchTerm + "\"")
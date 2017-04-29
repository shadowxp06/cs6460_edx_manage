#!/usr/bin/python
#
# Last Updated: 04/09/2017 11:52 AM/EST
#
import Constants
import os
import MiscUtils

class MySQL(object):
    def __init__(self):
        self.command = ""
        self.totalArgs = len(self.args)

    def __init__(self,command):
        self.command = command
        self.totalArgs = len(self.args)

    def __init__(self,command,args):
        self.command = command
        self.args = args
        self.totalArgs = len(self.args)

    def do_action(self):
        if self.command == 'change_root_password':
             user = self.args[3]
             strQuery = 'mysql -u root -p -e "SET PASSWORD FOR ' + user + "@'localhost' = PASSWORD('" + self.args[4] + "');"
             os.system("sudo " + strQuery)
             MiscUtils.write_to_log(Constants.mgmt_system_log,
                                    MiscUtils.get_current_user() + " " + Constants.change_user_pass + " " + self.args[4])
#!/usr/bin/python
#
# Last Updated: 04/15/2017 9:21 PM/EST
#

#TODO List:
import Constants
import os
import MiscUtils


class User(object):
    def __init__(self):
        self.command = ""

    def __init__(self, command):
        self.command = command

    def __init__(self, command, args):
        self.command = command
        self.args = args
        self.totalLen = len(args)

    def do_command(self):
        if self.command == "add_edx_superuser":
            if self.totalLen > 4:
                print(Constants.header + Constants.add_edx_user)
                self.add_user(self.args[3], self.args[4], True, True)
                print(Constants.header + Constants.done)
                MiscUtils.write_to_log(Constants.mgmt_system_log,
                                       MiscUtils.get_current_user() + " " + Constants.add_edx_user_log + " " + self.args[3] + " " + self.args[4])
        elif self.command == "add_edx_user":
            print(Constants.header + Constants.add_edx_user)
            self.add_user(self.args[3], self.args[4], False, False)
            print(Constants.header + Constants.done)
            MiscUtils.write_to_log(Constants.mgmt_system_log,
                                   MiscUtils.get_current_user() + " " + Constants.add_edx_user_log + " " + self.args[
                                       3] + " " + self.args[4])
        elif self.command == "add_edx_staff":
            print(Constants.header + Constants.add_edx_user)
            self.add_user(self.args[3], self.args[4], True, False)
            print(Constants.header + Constants.done)
            MiscUtils.write_to_log(Constants.mgmt_system_log,
                                   MiscUtils.get_current_user() + " " + Constants.add_edx_user_log + " " + self.args[
                                       3] + " " + self.args[4])
        elif self.command == "delete_edx_user":
            print(Constants.not_implemented_message)
        elif self.command == "change_password":
            print(Constants.not_implemented_message)
        else:
            print(Constants.command_not_found)

    def add_user(self,username, email, isStaff, isSuperUser):
        cmd = "sudo /edx/bin/python.edxapp /edx/bin/manage.edxapp lms manage " + username + " " + email

        if isStaff:
            cmd = cmd + " --staff"

        if isSuperUser:
            cmd = cmd + " --superuser"

        cmd = cmd + " --settings=aws"

        if MiscUtils.isValidEmail(email):
            os.system(cmd)
        else:
            print(Constants.openedx_user_add_invalidemail)
#
# Last Updated: 03/11/2017 3:33 PM/EST
#
#
# This is to handle the Supervisor commands coming in/out of the program
import os
import Constants
import MiscUtils


class Supervisor(object):
    __sv__ = "sudo /edx/bin/supervisorctl"

    def __init__(self,command):
        self.cmd = command

    def run(self):
        os.system(self.__sv__ + " " + self.cmd)
        MiscUtils.write_to_log(Constants.mgmt_system_log, MiscUtils.get_current_user() + " " + Constants.supervisor_log + " " + self.cmd)


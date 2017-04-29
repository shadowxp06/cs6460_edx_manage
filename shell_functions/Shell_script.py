#
# Last Updated: 04/09/2017 12:04 PM/EST
#
#
# This is to handle Shell Scripts

import os
import Constants
import MiscUtils


class Shell_Script(object):
    def __init__(self, directory, script_name):
        self.dir = directory
        self.script = script_name

    def __does_script_exist(self):
        return os.path.exists(self.dir + self.script)

    def run_script(self):
        if self.__does_script_exist():
            os.system(self.dir + self.script)
            MiscUtils.write_to_log(Constants.mgmt_system_log, MiscUtils.get_current_user() + " " + Constants.execute_shell_script + " " + self.dir + self.script)
        else:
            print(Constants.script_not_found)

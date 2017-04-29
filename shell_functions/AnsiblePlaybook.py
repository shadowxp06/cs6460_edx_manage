#!/usr/bin/python
#
# Last Updated: 04/15/2017 10:11 PM/EST
#

import Constants
import os
import MiscUtils


class AnsiblePlaybook(object):
    __ansible__command__ = "cd /edx/app/edx_ansible/edx_ansible/playbooks/edx-east && sudo /edx/app/edx_ansible/venvs/edx_ansible/bin/ansible-playbook -i localhost, -c local "

    def __init__(self):
        self.pb = ""

    def __init__(self, pb):
        self.pb = pb

    def run_playbook(self):
        os.system(self.__ansible__command__ + " " + self.pb)
        MiscUtils.write_to_log(Constants.mgmt_system_log, MiscUtils.get_current_user() + Constants.openedx_run_playbook + self.pb)
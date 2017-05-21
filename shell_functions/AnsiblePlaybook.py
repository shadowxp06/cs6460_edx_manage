#!/usr/bin/python
#
# Last Updated: 05/20/2017 9:36 PM/EST
#

import Constants
import os
import MiscUtils

ansible_ext = ".yml"
ansible_playbooks_dir = "/gt/playbooks/edx-east/"

class AnsiblePlaybook(object):
    __ansible__command__ = "sudo /edx/app/edx_ansible/venvs/edx_ansible/bin/ansible-playbook -i localhost, -c local " + ansible_playbooks_dir

    def __init__(self):
        self.pb = ""

    def __init__(self, pb):
        self.pb = pb

    def check_for_extension(self):
        if ansible_ext not in self.pb:
            self.pb = self.pb + ".yml"

    def run_playbook(self):
        self.check_for_extension()
        os.system(self.__ansible__command__ + " " + self.pb)
        MiscUtils.write_to_log(Constants.mgmt_system_log, MiscUtils.get_current_user() + Constants.openedx_run_playbook + self.pb)
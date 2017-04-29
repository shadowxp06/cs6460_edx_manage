#
# Last Updated: 04/21/2017 10:13 PM/EST
#
#
# This is to handle the System Updates portion
import os
import Constants
import MiscUtils


class System_Updates(object):
    packages = ['libxml2-dev', 'libxslt1-dev', 'python-pip', 'libmysqlclient-dev','python-apt',
                'python-dev','libxmlsec1-dev','libfreetype6-dev','swig','python2.7',
                'python2.7-dev','python-yaml','python-jinja2','libmysqlclient-dev','elasticsearch'
                ,'mongodb-org','rabbitmq-server']

    def __init__(self, do_mark, do_upgrade):
        self.do_mark_packages = do_mark
        self.do_upgrade = do_upgrade

    def run_mark_packages(self):
        if self.do_mark_packages:
            print(Constants.header + Constants.system_updates_mark_package)
            for item in self.packages:
                os.system("sudo apt-mark hold " + item)
            print(Constants.header + Constants.done)
            MiscUtils.write_to_log(Constants.mgmt_system_log,
            MiscUtils.get_current_user() + " " + Constants.system_updates_mark_package_log)
        else:
            print(Constants.header + Constants.done)
            MiscUtils.write_to_log(Constants.mgmt_system_log, MiscUtils.get_current_user() + " " + Constants.system_updates_mark_package_log_unsuccessful)

    def run_upgrades(self):
        if self.do_upgrade:
            print(Constants.header + Constants.system_updates_run_upgrades)
            os.system("sudo apt-get update -y && apt-get upgrade -y && apt-get autoremove")
            print(Constants.header + Constants.done)
            MiscUtils.write_to_log(Constants.mgmt_system_log,
                                   MiscUtils.get_current_user() + " " + Constants.system_updates_run_upgrades_successful)
        else:
            print(Constants.header + Constants.done)
            MiscUtils.write_to_log(Constants.mgmt_system_log,
                                   MiscUtils.get_current_user() + " " + Constants.system_updates_run_upgrades_unsuccessful)

    def run_all(self):
        self.run_mark_packages()
        self.run_upgrades()

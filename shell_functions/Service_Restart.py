#
# Last Updated: 04/15/2017 10:08 PM/EST
#
#
# This is to handle the Services Restart portion
import os
import Constants
import Supervisor
import MiscUtils


class Service_Restart(object):
    def __init__(self,svc):
        self.service = svc

    def restart_service(self):
        print(Constants.header + self.service + " " + Constants.restart)
        if self.service == "forum":
            self.__openedx__forum__res()
        elif self.service == "mongodb" or self.service == "mongo" or self.service == "mongod":
            self.__mongodb__res()
        elif self.service == "ssh":
            self.__ssh__res()
        elif self.service == "nginx":
            self.__nginx__res()
        elif self.service == "denyhosts":
            self.__denyhosts__res()
        elif self.service == "mysql":
            self.__mysql__res()
        elif self.service == "nginx":
            self.__nginx__res()
        elif self.service == "all":
            self.__openedx__res()
            self.__openedx__analytics__res()
            self.__openedx__certs__res()
            self.__openedx__ecommerce__res()
            self.__openedx__ecomworker__res()
            self.__openedx__insights__res()
            self.__openedx__notifier_celery__res()
            self.__openedx__notifier_scheduler__res()
            self.__openedx__programs__res()
            self.__openedx__xqueue__res()
            self.__openedx__xqueue_consumer__res()
            self.__mongodb__res()
            self.__ssh__res()
            self.__nginx__res()
            self.__denyhosts__res()
            self.__mysql__res()
            self.__nginx__res()
        elif self.service == "edxapp":
            self.__openedx__edxapp__res()
        elif self.service == "analytics_api":
            self.__openedx__analytics__res()
        elif self.service == "certs":
            self.__openedx__certs__res()
        elif self.service == "ecommerce":
            self.__openedx__ecommerce__res()
        elif self.service == "ecommerce_workers":
            self.__openedx__ecomworker__res()
        elif self.service == "insights":
            self.__openedx__insights__res()
        elif self.service == "notifier-celery-workers":
            self.__openedx__notifier_celery__res()
        elif self.service == "notifier-scheduler":
            self.__openedx__notifier_scheduler__res()
        elif self.service == "programs":
            self.__openedx__programs__res()
        elif self.service == "xqueue":
            self.__openedx__xqueue__res()
        elif self.service == "xqueue_consumer":
            self.__openedx__xqueue_consumer__res()
        elif self.service == "rabbitmq":
            self.__rabbitmq_server__res()
        elif self.service == "edxapp-worker" or self.service == "edxapp-workers" or self.service == "edxapp_worker" or self.service == "edxapp_workers":
            self.__openedx__edxapp_worker__res()
        else:
            print(Constants.option_not_found)
        print(Constants.header + Constants.done)
        MiscUtils.write_to_log(Constants.mgmt_system_log, MiscUtils.get_current_user() + " " + Constants.restart_log + " " + self.service)

    def __openedx__res(self):
        self.__openedx__edxapp__res()
        self.__openedx__edxapp_worker__res()

    def __openedx__analytics__res(self):
        sv = Supervisor.Supervisor("restart")
        sv.cmd = sv.cmd + " analytics_api:"
        sv.run()

    def __openedx__certs__res(self):
        sv = Supervisor.Supervisor("restart")
        sv.cmd = sv.cmd + " certs:"
        sv.run()

    def __openedx__ecommerce__res(self):
        sv = Supervisor.Supervisor("restart")
        sv.cmd = sv.cmd + " ecommerce:"
        sv.run()

    def __openedx__ecomworker__res(self):
        sv = Supervisor.Supervisor("restart")
        sv.cmd = sv.cmd + " ecomworker:"
        sv.run()

    def __openedx__edxapp__res(self):
        sv = Supervisor.Supervisor("restart")
        sv.cmd = sv.cmd + " edxapp:"
        sv.run()


    def __openedx__edxapp_worker__res(self):
        sv = Supervisor.Supervisor("restart")
        sv.cmd = sv.cmd + " edxapp_worker:"
        sv.run()

    def __openedx__forum__res(self):
        sv = Supervisor.Supervisor("restart")
        sv.cmd = sv.cmd + " forum:"
        sv.run()

    def __openedx__insights__res(self):
        sv = Supervisor.Supervisor("restart")
        sv.cmd = sv.cmd + " insights:"
        sv.run()

    def __openedx__notifier_celery__res(self):
        sv = Supervisor.Supervisor("restart")
        sv.cmd = sv.cmd + " notifier-celery-workers:"
        sv.run()

    def __openedx__notifier_scheduler__res(self):
        sv = Supervisor.Supervisor("restart")
        sv.cmd = sv.cmd + " notifier-scheduler:"
        sv.run()

    def __openedx__programs__res(self):
        sv = Supervisor.Supervisor("restart")
        sv.cmd = sv.cmd + " programs:"
        sv.run()

    def __openedx__xqueue__res(self):
        sv = Supervisor.Supervisor("restart")
        sv.cmd = sv.cmd + " xqueue:"
        sv.run()

    def __openedx__xqueue_consumer__res(self):
        sv = Supervisor.Supervisor("restart")
        sv.cmd = sv.cmd + " xqueue_consumer:"
        sv.run()

    def __mongodb__res(self):
        os.system("sudo service mongod restart")

    def __ssh__res(self):
        os.system("sudo service sshd restart")

    def __nginx__res(self):
        os.system("sudo service nginx restart")

    def __denyhosts__res(self):
        os.system("sudo service denyhosts restart")

    def __mysql__res(self):
        os.system("sudo service mysql restart")

    def __nginx__res(self):
        os.system("sudo service nginx restart")

    def __rabbitmq_server__res(self):
        os.system("sudo /etc/init.d/rabbitmq-server restart")
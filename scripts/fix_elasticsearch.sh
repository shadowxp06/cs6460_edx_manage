#!/usr/bin/env bash
#
#This script was created to re-run the ElasticSearch role
#
# Last Updated: 03/31/2017 4:56 PM/EST
#
#**This is not to be run by the Python manage.py script -- Run this BY HAND**
#**This script may not be needed in most cases**

#THis script is NOW unsupported - use /gt/manage.py run-ansible-playbook <playbook> -- this script is being kept here as an example

cd /edx/app/edx_ansible/edx_ansible/playbooks/edx-east
/edx/app/edx_ansible/venvs/edx_ansible/bin/ansible-playbook -i localhost, -c local forum.yml

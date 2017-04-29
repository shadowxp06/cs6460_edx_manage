#!/usr/bin/python
#
# Last Updated: 04/15/2017 4:46 PM/EST
#

import sys
import shell_functions
import Constants
import help

lastrevision = "04/15/2017 4:46 PM/EST"

# Get the total number of args passed to the demo.py
total = len(sys.argv)

# Get the arguments list
cmdargs = str(sys.argv)

## Source: https://www.cyberciti.biz/faq/python-command-line-arguments-argv-example/ (NixCraft)
if total > 1:
    firstArg = str(sys.argv[1]).lower()
    if firstArg == "restart":
        total_second = len(sys.argv)
        if total_second > 2:
            secondArg = sys.argv[2]
            svc = shell_functions.Service_Restart("")
            svc.service = str(secondArg).lower()
            svc.restart_service()
        else:
            print(Constants.option_not_found)
    elif firstArg == "do":
        total_second = len(sys.argv)
        if total_second > 2:
            secondArg = sys.argv[2]
            svc = shell_functions.Do(secondArg, sys.argv) #at least in this instance, this ensures that the 2nd arg is always an array
            svc.do_command()
        else:
            print(Constants.option_not_found)
    elif firstArg == "run-ansible-playbook":
        total_second = len(sys.argv)
        if total_second > 2:
            secondArg = sys.argv[2]
            svc = shell_functions.AnsiblePlaybook(secondArg)
            svc.run_playbook()
    elif firstArg == "user":
        svc = shell_functions.User(sys.argv[2], sys.argv)
        svc.do_command()
    elif firstArg == "help":
        secondTotal = len(sys.argv)
        if secondTotal > 2:
            secondArg = str(sys.argv[2])
            csv = help.CSV("help.csv")
            csv.list_command(secondArg.lower())
        else:
            csv = help.CSV("help.csv")
            csv.list_all()
    elif firstArg == "mysql":
        print(Constants.not_implemented_message)
    elif firstArg == "generate-random-pass":
        svc = shell_functions.Shell_Script(shell_functions.get_script_dir(), "generate_random_pass.sh")
        print(svc.run_script())
    elif firstArg == "about":
        print("-- GT Manage.py --")
        print("version 1.0 - Last Revision: " + lastrevision)
        print("------------------")
        print("This utility is used for the management of the Open EdX VM used by the CS6460 course at Georgia Tech")
    elif firstArg == "delete_course":
        if len(sys.argv) > 2:
            shell_functions.do_delete_course(sys.argv[2])
    else:
        print(Constants.command_not_found)

else:
    print(Constants.command_not_found)


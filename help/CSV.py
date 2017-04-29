#!/usr/bin/python
#
# Last Updated: 03/12/2017 4:41 PM/EST
#
import shell_functions
import Constants
import csv
import os

class CSV(object):
    def __init__(self):
        self.filename = ""

    def __init__(self, filename):
        self.filename = filename


    def get_usage(self,command):
        with open(os.path.join(shell_functions.get_python_dir(),"help",Constants.help_csv)) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['command'] == command:
                    self.usage = row['usage']

    def get_purpose(self, command):
        with open(os.path.join(shell_functions.get_python_dir(),"help",Constants.help_csv)) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['command'] == command:
                    self.usage = row['purpose']

    def list_command(self, command):
        with open(os.path.join(shell_functions.get_python_dir(),"help",Constants.help_csv)) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['command'] == command:
                    print("-- " + row['command'] + " --")
                    print("Usage: " + row['usage'])
                    print("Purpose: " + row['purpose'])

    def list_all(self):
        print(Constants.header + " Commands")
        print("----")
        #shell_functions.get_python_dir() + "\\help\\" + Constants.help_csv
        with open(os.path.join(shell_functions.get_python_dir(),"help",Constants.help_csv)) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['command'] + " - " + row['purpose'])

        print("----")
        print(Constants.msg_for_more_help)

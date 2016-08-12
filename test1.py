#!/usr/bin/env python

import shlex
from subprocess import Popen, PIPE
import six
import prettytable

def get_exitcode_stdout_stderr(cmd):
    """
    Execute the external command and get its exitcode, stdout and stderr.
    """
    args = shlex.split(cmd)

    proc = Popen(args, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    exitcode = proc.returncode
    #
    return exitcode, out, err

def output_to_screen(cmd, out):

    print("command\n%s" % cmd)
    print("output\n%s" % out)

def parse_output(output):
    fields = []
    data_dict = {}
    count = 0
    lines = [s for s in output.split('\n') if s]
    for line in lines:
        if "+---" in line:
            continue
        if count == 0:
            fields = line.split("|")
            fields = [x.strip(' ') for x in fields]
            fields = [x for x in fields if x != ''] 
            print ("fields:\n%s" % fields)
            count += 1
        else:
            data_row = line.split("|")
            data_row = [x.strip(' ') for x in data_row]
            data_row= [x for x in data_row if x != ''] 
            print data_row

def sanity_check():

    cmd = "cinder --os-volume-api-version 3.11 cluster-list --detail"
    exitcode, out, err = get_exitcode_stdout_stderr(cmd)
    output_to_screen(cmd, out)
    columns = ['Name', 'Binary', 'State', 'Status']
    parse_output(out)
    #print pt
#    print_list(out, columns)
#    utils.print_list(vtypes, ['ID', 'Name', 'extra_specs'])



def main():
    sanity_check()

if __name__ == '__main__':
    main()

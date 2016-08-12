#!/usr/bin/env python

import shlex
from subprocess import Popen, PIPE

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

def sanity_check():

    cmd = "cinder --os-volume-api-version 3.11 cluster-list --detail"
    exitcode, out, err = get_exitcode_stdout_stderr(cmd)
    output_to_screen(cmd, out)


def main():
    sanity_check()

if __name__ == '__main__':
    main()

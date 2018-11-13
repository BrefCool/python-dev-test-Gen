""" This is a unittest file for {0}.py
Copyright 2018 Yuxuan Su syx525@bu.edu
"""

import unittest
import subprocess
import {0}

PROGRAM_TO_TEST = ""    # set program to test if needed
TIMEOUT = 10    # set timeout(seconds)


def runprogram(self, program, args, inputstr):
    """ run a program and get result: wrapper for subprocess.run """
    try:
        err=""
        coll_run = subprocess.run(
            [program, *args],
            input=inputstr.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout = TIMEOUT)
    except Exception as e:
       err=str(e)
    finally:
        if err:
            self.fail(err)

    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    program_errors = coll_run.stderr.decode()
    return (ret_code, program_output, program_errors)


class {0}TestCase(unittest.TestCase):
    """ This is where you design your unit test cases """

def main():
    print("start testing {0}.py ....")
    unittest.main()

if __name__ == "__main__":
    main()
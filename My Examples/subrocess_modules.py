#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 03:01:58 2018

@author: manana
"""

import subprocess

command = ["ping", "8.8.8.8 -c 5 -n"]
#command = "pwd"

o = subprocess.run(command)
result_msg = """Executing command from Python script gives us the following result.\n 
    The return code: {}\n 
    The output of the command (from stdout): + {}\n
    The stderr: {}\n"""

print(result_msg.format(o.returncode, o.stdout, o.stderr))
                           

#!/usr/bin/env python3 

import subprocess
import os

os.system("df -h | grep '/$' | awk '{print $4}'")
def free_space():
	A = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output = A.communicate()
	return output[0].decode('utf-8').strip()
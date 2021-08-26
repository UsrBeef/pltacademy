"""
collect into "/tmp/investigation/" list of all the files accessed by java processes.
in the directory - create one file with list of accessed files per each process.
filename = access_$PID.txt
"""
import os
os.system("mkdir /tmp/investigation | lsof -c java > /tmp/investigationfile.txt")

#here i used commands for cration new directory and getting info about java processes
#have no idea  how to format output for now
"""
collect into "/tmp/investigation/" list of all the files accessed by java processes.
in the directory - create one file with list of accessed files per each process.
filename = access_$PID.txt
"""
import os
os.system("mkdir /tmp/investigation | lsof -c java > /tmp/investigation/file.txt")

f = open(r'E:\pltproject\file.txt', mode= 'r', encoding='utf-8')
l = []
for i in f:
    l.append(i.split())
for i in range(1,len(l)):
    print('PID = ',l[i][0],'file = ',l[i][2])
#here i used commands for cration new directory and getting info about java processes

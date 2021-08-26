"""
 create a script that corrects one server name (f.e. change nginx-01.com to nginx-02.com)
 in 100 configuration files on linux server in one directory
"""
import os
f1 = open("nginx.conf", "rt")
f2 = open("nginxnew.conf", "wt") #used two files. 1 is original .conf, 2 - its changed copy
for line in f1:
	f2.write(line.replace('nginx-01.com', 'nginx-02.com'))
f1.close() #close input and output files
f2.close()
os.system('rm nginx.conf | mv "nginxnew.conf" "nginx.conf" ') #delete old file and rename new one
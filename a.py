"""
 create a script that corrects one server name (f.e. change nginx-01.com to nginx-02.com)
 in 100 configuration files on linux server in one directory
"""
import os
import re

dir = os.listdir(r'E:\pltproject\dir') #get the content of \dir in LIST

for i in dir:
    open_file = open(i, 'r') #open file
    read_file = open_file.read() #read file
    regex = re.compile('nginx-01.com') #using regular expression to search for 'nginx-01.com'
    read_file = regex.sub('nginx-02.com', read_file) # using regular expression to replace 'nginx-01.com' with 'nginx-02.com'
    write_file = open(i, 'w') #write
    write_file.write(read_file)

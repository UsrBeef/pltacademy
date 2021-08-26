"""
Create and Schedule a script that creates 10 files named "test_$TIMESTAMP_$NUM.txt"
(timestamp == current_time, num == 1..10) each one containing 1000 random characters.
in the comments write us how do you plan to schedule it to run every 6 hours.
"""
import random, string, datetime

filename = datetime.datetime.now() #get date
f1 = open("ctr.txt","r") #get counter with "len" function
for line in f1:
    ctr = len(line)
f1.close()

f1 = open("ctr.txt","a") #update counter
f1.write("1")
f1.close()

#create new file and writing 1000 random characters
f = open("test_" + filename.strftime("%H %M %S") + "_%d.txt" %ctr, "w")
f.write(''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(1000)))
f.close()

#shedule with cron
# command: 0 */6 * * * [script location]
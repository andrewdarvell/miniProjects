# coding: utf8
#!/usr/bin/env python
import os,subprocess

#result = os.listdir("/home/darvell/")
#for res in result:
	#print res
	
#Команда 1
uname = "uname"
uname_arg = "--a"
print "Gathering system information with %s command:\n" % uname
subprocess.call([uname, uname_arg])
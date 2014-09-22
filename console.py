# coding: utf8
import subprocess, commands, string

#list = subprocess.call(["ls", "-l"])


#commandString = "ls -l"
#commandOutput = commands.getoutput(commandString)
#findResults = string.split(commandOutput, "\n")
#print type(findResults)

#for item in findResults:
	#print "-----"
	#print item

result = subprocess.call("cd /home/darvell/SVN/docs",shell=True)
subprocess.call("svn update" ,shell=True)
print result
	

#!/usr/bin/python
import os
import sys

print "zero argument : ", sys.argv[0]
print "1st argument : ", sys.argv[1]
print "2ns argument : ", sys.argv[2]

folderName = sys.argv[1]
#folderName = "/tmp/awadhesh/demo1/"
fileName = sys.argv[2]
#fileName = "app1.log"
#Folder validation
folderPathValidation = os.path.isdir(folderName) 
print "output of folderPathValidation : ", folderPathValidation
if folderPathValidation:
	print "Folder path exists"
else:
	print "Foler path donot exists"
	os.system("mkdir -p " + folderName)

#File validation
filePath = folderName + '/' + fileName 
fileValidation = os.path.exists(filePath)
print "output of fileValidation : ", fileValidation

if fileValidation:
	print "File does exists"
	os.system("chmod 640 " + filePath)
else:
	print "File doesnot exists"
	os.system("touch " + filePath)
	os.system("chmod 640 " + filePath)
		
	




#! /usr/bin/python
import sys

print "Hello world!!!"
myVar = 10
myVar1 = "Devops"
myVar2 = 12.0
mysum = myVar1 + str(3.5)
mysum1 = "dev" + "ops"
mysum2 = "devops" + str(8)
print mysum2
print mysum1
print mysum
print "my first variable : " + str(myVar)
print "my first variable : ", myVar
print "my second variable : " + myVar1
print "My third variable : " + str(myVar2)

userinput1 = sys.argv[1]
userinput2 = sys.argv[2]

print userinput1
print userinput2
#userinput3 = raw_input("please provide your name\n")
#print "My name : ", userinput3
#userinput = sys.argv
#print userinput

sum1 = int(userinput1) + int(userinput2)
print sum1

if (sum1 > 100):
	print "I got 100"
else:
	print "Still way behind !!!"

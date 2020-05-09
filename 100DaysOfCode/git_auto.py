#!/usr/bin/python3

import subprocess as sp

import os

print('''1 for add file
	2 for check status of file's''')
num = input("enter number")

if num == '1':
	print(sp.getoutput('git add .'))

elif num== '2':
	print(sp.getoutput('git status'))
else:
	print("choose right number")	






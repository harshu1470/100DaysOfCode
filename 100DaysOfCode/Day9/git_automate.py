#!/usr/bin/python3

import subprocess as sp

import os

print('''1 for add file
2 for check status of file's
3 for commit
4 for check logs
5 for push to github by master branch
6 for push to github by another branch
7 for add file by specifying file name
8 for do all things together''')
num = input("enter number")

def push_git():
	print(sp.getoutput('git add .'))
	discription = input("enter your commit message")
	print(sp.getoutput('git commit -m ' + discription))
	print(sp.getoutput('git push origin master'))
while True:
	if num == '1':
		print(sp.getoutput('git add .'))

	elif num == '2':
		print(sp.getoutput('git status'))
	elif num == '3':
		discription = input("enter your commit message")
		print(sp.getoutput('git commit -m '+ discription))
		print(sp.getoutput('git log -p -2'))
	elif num == '4':
		print(sp.getoutput('git log'))
	elif num == '5':
		print(sp.getoutput('git push origin master'))

	elif num == '6':
		branch_name = input("enter you branch name to checkout")
		print(sp.getoutput('git checkout ' + branch_name ))
		print(sp.getoutput('git push origin ' + branch_name))
	elif num == '7':
		file_name =input("enter your file name")
		print(sp.getoutput('git add ' + file_name))

	elif num == "8":
		push_git()
		break




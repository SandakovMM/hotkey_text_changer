#!/usr/bin/python
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE

# Get all commits where commit message contains string in
def git_all_task_commits(string_in):
	task_number = string_in
#'git log --all --grep="' + string_in + '" --pretty=format:"%ad:%an:%d:%B"' <-- if you want commits from all branches
	command='git log --grep="' + string_in + '" --pretty=format:"%h:%B"'
	proc = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
	proc.wait()
	res = proc.communicate()
	if proc.returncode:
		print res[1]
	return res[0]
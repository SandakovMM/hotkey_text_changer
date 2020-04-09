#!/usr/bin/python
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from function_loader import register

# Get all commits where commit message contains string in
def git_all_task_commits_to_markdown(string_in, project_path):
	task_number = string_in
#'git log --all --grep="' + string_in + '" --pretty=format:"%ad:%an:%d:%B"' <-- if you want commits from all branches
	command='git log --grep="' + string_in + '"'
	proc = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
	proc.wait()
	res = proc.communicate()

	result_string = ""
	# I want to add link to eltex gitlab for commit here
	for one_string in res[0].split("\n"):
		if one_string[:6] == "commit":
			commit_link = "\"" + one_string[7:] + "\"" + project_path + one_string[7:]
			one_string = "commit " + commit_link
		result_string += one_string + "\n"

	if proc.returncode:
		print res[1]
	return '{{collapse(Коммиты по задаче)\n' + result_string +'}}'
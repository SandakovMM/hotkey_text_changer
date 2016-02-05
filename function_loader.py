#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from pprint import pprint

# One command. Hope we can use something like function pointer
class Command:
	def __init__(self, name, key, command):		
		self.name = name
		self.key = key
		self.function = command

	def show(self):
		print self.name + ' ' + self.key + ': ' + self.command	

# We use json to show what functions to use and from where
# This class also store all modules what we already importe. This is needed cas in real
# i don't really know what python gonna do if we import some module what we already import earlier.
class FunctionLoader:
	def __init__(self):
		self.all_commands = []
		self.addition_modules = []
		with open('actions.json') as data_file:
			data = json.load(data_file)
		for command in data["commands"]:
			function_to_call = self.load_command(command["module"], command["command"])
			tmp_cmd = Command(command["name"], command["key"], function_to_call)
			self.all_commands.append(tmp_cmd)

	def find_module(self, module_name):
		for module in self.addition_modules:
			if module.__name__ == module_name:
				return module
		return None

	def find_command_by_key(self, key):
		for command in self.all_commands:
			if command.key == key:
				return command.function
		raise Exception('not found', key)

	# There we need to load function from module and return this function
	def load_command(self, module, command):
		m = self.find_module(module)		
		if m == None:
			m = __import__(module)
			self.addition_modules.append(m)
		return getattr(m, command)

	# This function used to return all commands visable data (names and keys)
	#  to show this data in our user intarface. Returns list of strings [name - key].
	def get_commands_visable_data(self):
		result = []
		for command in self.all_commands:
			result.append(command.name + ' - ' + command.key)
		return result

	# This function used to get all hotkeys, what we can use.
	def get_all_hotkeys(self):
		result = []
		for command in self.all_commands:
			result.append(command.key)
		return result
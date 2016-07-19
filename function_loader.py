#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from pprint import pprint
import sys

# One command. Hope we can use something like function pointer
class Command:
	def __init__(self, name, key, command):		
		self.name = name
		self.key = key
		self.function = command

	def __call__(self, *args, **kwargs):
		return self.function(*args, **kwargs)

	def show(self):
		print self.name + ' ' + self.key + ': ' + self.command	

# This class filed functions over decorators. So we don't need to use any
# json files, just say use function in module and go on.
class FunctionStorage(object):
	def __init__(self):
		self.all_commands = []

	def add_command(self, name, key, command):
		self.all_commands.append(Command(name, key, command))

	def find_command_by_key(self, key):
		for command in self.all_commands:
			if command.key == key:
				return command
		raise Exception('not found', key)

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


# We use json to show what functions to use and from where
# This class also store all modules what we already importe. This is needed cas in real
# i don't really know what python gonna do if we import some module what we already import earlier.
class FunctionLoader(FunctionStorage):
	def __init__(self, module_path):
		super(FunctionLoader, self).__init__()
		self.addition_modules = []
		self.modules_path = module_path

		sys.path.append(self.modules_path) # Add path to all modules

		with open(self.modules_path + 'actions.json') as data_file:
			data = json.load(data_file)
		for command in data["commands"]:
			function_to_call = self.load_command(command["module"], command["command"])
			self.add_command(command["name"], command["key"], function_to_call)

	def find_module(self, module_name):
		for module in self.addition_modules:
			if module.__name__ == module_name:
				return module
		return None

	# There we need to load function from module and return this function
	def load_command(self, module, command):
		m = self.find_module(module)		
		if m == None:
			m = __import__(module)
			self.addition_modules.append(m)
		return getattr(m, command)

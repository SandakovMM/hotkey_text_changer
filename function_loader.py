
import json
from pprint import pprint

# One command. Hope we can use something like function pointer
class Command:
	def __init__(self, name, key, command):		
		self.name = name
		self.key = key
		self.command = command
		#self.command_func

	def show(self):
		print self.name + ' ' + self.key + ': ' + self.command

# We use json to show what functions to use and from where
# This class also store all modules what we already importe. This is needed cas in real
# i don't really know what python gonna do if we import some module what we already import earlier
# 	
class FunctionLoader:
	def __init__(self):
		self.all_commands = []
		self.addition_modules = []
		with open('actions.json') as data_file:
			data = json.load(data_file)
		for command in data["commands"]:
			function_to_call = self.load_command(command["module"], command["command"])
			tmp_cmd = Command(command["name"], command["key"], command["module"] + '->' + command["command"])
			self.all_commands.append(tmp_cmd)

	def find_module(self, module_name):
		for module in self.addition_modules:
			if module.__name__ == module_name
				return module
		return None

	# There we need to load function from module and return this function
	def load_command(self, module, command):
		m = find_module(module)		
		if m == None:
			m = __import__(module)
			self.addition_modules.append(m)
		return getattr(m, command)

fl = FunctionLoader()
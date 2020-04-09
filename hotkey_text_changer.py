#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import function_loader
import sys
from changers import *

class MainWindow:
	def __init__(self, modules_path):
		self.root = Tk()
		self.root.geometry("130x500+900+200")
		self.count = 0
		self.modules_path = modules_path

		self.func_loader = function_loader.FunctionStorage()

		# Add listbox for user. TODO: set size of listbox to fill full window
		self.listbox = Listbox(self.root, width=900, height=900)
		self.listbox.pack()

		[self.listbox.insert(END, data_string)
			for data_string in self.func_loader.get_commands_visable_data()]

		# init hotkeys
		[self.root.bind_all("<" + key + ">", self.hotkey_reaction)
			for key in self.func_loader.get_all_hotkeys()]

		self.root.mainloop()

	def hotkey_reaction(self, event):
		result_str = ''
		try:			
			geted_str  = self.root.clipboard_get()	
			function = self.func_loader.find_command_by_key(event.char)
			result_str = function(geted_str)
			self.root.clipboard_clear()
			self.root.clipboard_append(result_str)
		except:
			result_str = 'Nothing to show!'
		self.create_hint(result_str)
		# We want to quit programm when work is done. Don't really shure thats
		#  leave it here or not. Problem is - after end of work clipboard make clear
		#  and we can't use changed string.
		#self.root.after(6000, self.root.destroy)

	def create_hint(self, out_str):
		hint_to_show = Hint(self.root)
		hint_to_show.set_out_string(out_str)
		hint_to_show.hint_lifecycle()


class Hint(Toplevel):
	'''A toplevel widget with the ability to fade in'''
	def __init__(self, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)

		# need to choose place depending on monitor sizes
		self.geometry("500x50+780+30")
		self.attributes("-alpha", 0.0)
		self.overrideredirect(1)
		self.hint_textbox = Text(self)
		self.hint_textbox.pack()

	def set_out_string(self, out_string):
		self.hint_textbox.insert(INSERT, out_string)

	def hint_lifecycle(self):
		self.fade_in()
		self.after(3000, self.fade_out)

	def fade_in(self):
		alpha = self.attributes("-alpha")
		if alpha == 1:
			alpha = 0
		alpha = min(alpha + .01, 1.0)
		self.attributes("-alpha", alpha)
		if alpha < 1.0:
			self.after(10, self.fade_in)

	def fade_out(self):		
		alpha = self.attributes("-alpha")

		alpha = max(alpha - .01, 0)
		self.attributes("-alpha", alpha)
		if alpha > 0:
			self.after(10, self.fade_out)
		if alpha == 0:
			self.destroy()

if __name__ == "__main__":
	if 1 == len(sys.argv):
		main = MainWindow("")
	else:
		# we get path of json and modules as arguments, so use it
		main = MainWindow(sys.argv[1])
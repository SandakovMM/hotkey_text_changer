#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import function_loader

class MainWindow:
	def __init__(self):
		self.root = Tk()
		self.root.geometry("100x500+900+200")
		self.count = 0
		self.func_loader = function_loader.FunctionLoader()

		# Add listbox for user. TODO: set size of listbox to fill full window
		self.listbox = Listbox(self.root)
		self.listbox.pack()
		for data_string in self.func_loader.get_commands_visable_data():
			self.listbox.insert(END, data_string)

		# init hotkeys
		for key in self.func_loader.get_all_hotkeys():
			self.root.bind_all("<" + key + ">", self.hotkey_reaction)

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
	main = MainWindow()
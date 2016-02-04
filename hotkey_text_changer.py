#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *

# There is a test string function
def string_function(string_in):
	result_string = ''
	for char_in in string_in:
		result_string = result_string + char_in + '.'
	return result_string

class MainWindow:
	def __init__(self):
		self.root = Tk()
		self.count = 0

		listbox = Listbox(self.root)
		listbox.pack()

		listbox.insert(END, "make some - q")

		# init hotkeys 
		self.root.bind_all("<q>", self.hotkey_reaction)
		self.root.mainloop()

	def hotkey_reaction(self, event):
		result_str = ''
		try:
			geted_str  = self.root.clipboard_get()
			result_str = string_function(geted_str)
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
		self.geometry("500x50+780+30")
		self.attributes("-alpha", 0.0)
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
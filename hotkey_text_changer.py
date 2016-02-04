#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *

class MainWindow:
	def __init__(self):
		self.root = Tk()
		self.count = 0
		listbox = Listbox(self.root)
		listbox.pack()

		# Check how it's look like
		listbox.insert(END, "create hint - q")
		listbox.insert(END, "fix if - f")
		listbox.insert(END, "somethig if - s")

		# init hotkeys 
		self.root.bind_all("<q>", self.create_hint)

		self.root.mainloop()

	def hotkey_reaction(self, event):
		pass

	def create_hint(self, event):
		self.count += 1
		t=Hint(self.root)
		t.wm_title("Window %s" % self.count)
		t.hint_lifecycle()


class Hint(Toplevel):
	'''A toplevel widget with the ability to fade in'''
	def __init__(self, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)
		self.attributes("-alpha", 0.0)

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
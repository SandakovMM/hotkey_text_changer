# hotkey_text_changer

This python programm to make any changes with text on keystroke. 
In my work i find out that sometimes i need to change some strings to another by a certain pattern. So now, i try to make programm to do that with just one or two keystroke.

In my mind now it's must be like that:
	We have some programm called with some hotkey in OS (or maybe it's always stay alive, don't really know whats best decision). We set mapping of keys and some functions worked with strings in addition modules attached with our programm. And after that we can use our hotkeys. Function get string from clipboard change it and insert result back to clipboard.

Find out that i can use linux console programm xsel in bash scripts. Just information for me :)

So this is it. Seems like pretty simple task. 
Tell me if you have some questions or advice.

------------------------ Update ---------------------
=D

Seems like it's start to work like i want to. For description hotkeys and change functions you need
to use action.json file. Structure ou this file is:
name    - it's a name of fuction or description what this function do. Displayed at opened window.
key     - it's a hotkey associated with function.
module  - python module where store function code.
command - function name in this module.

Module must be in same folder as a action.json file.

How to use script:
	You need to make command "python hotkey_text_changer.py" from and choose some option from opened
	window. After that use hotkey and enjoy. If you want to use action.json and modules from another
	folders, you can use argument of command line like this "python hotkey_text_changer.py [your_path]"


Thank you for attention and have a nice day!
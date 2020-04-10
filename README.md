# Text changer project

## hotkey_text_changer

This is a GUI version of python programm to make any changes with text on keystroke.
When you call a script GUI with tips shows up and you can choose some of keystroke and
change string what you copyed before from somewhere.

## How to add your own text changer

There is a folder named changers where you can add your own text changer module.
For description hotkeys and change functions you can use two ways of work.
* It's old version of configuration with action.json configs. You may find out how it's worked before commit ce676de. For use it you need to use action.json file. Structure ou this file is:

> name - it's a name of fuction or description what this function do. Displayed at opened window.
> key - it's a hotkey associated with function.
> module - python module where store function code.
> command - function name in this module.

Module must be in same folder as a action.json file.

* It's a new version of adding functions. I make it when i decided to try using python decorators. So sine using it you just need to add file with your actions to changers folder, add it to __init__.py in this folder and going to use @register decorator from function_loader.py on your function with arguments (description, key). Just like this:

```python
from function_loader import register

@register("Desription", "k")
def my_func(string_in)
```

That's all, now you can use your function with key 'k' to change you string.

How to use script:
	You need to make command "python hotkey_text_changer.py" from and choose some option from opened
	window. After that use hotkey and enjoy. If you want to use action.json and modules from another
	folders, you can use argument of command line like this "python hotkey_text_changer.py [your_path]"


Thank you for attention and have a nice day!

## cli_text_changer

This is a cli version of programm. It's can be used to make changes faster if you know your keystrokes.
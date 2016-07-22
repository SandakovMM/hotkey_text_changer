#!/usr/bin/python
# -*- coding: utf-8 -*-
# There is a default file to add some string changers functions
from function_loader import register

# There is a test string function
@register("Add dots", "q")
def string_add_dots(string_in):
	result_string = ''
	for char_in in string_in:
		result_string = result_string + char_in + '.'
	return result_string

@register("From eng to rus", "r")
def string_from_eng_to_ru(string_in):
	eng_str=u'qwertyuiop[]asdfghjkl;\'zxcvbnm,./`QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>~'
	ru_str =u'йцукенгшщзхъфывапролджэячсмитьбю.ёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
	result_string = ''

	for char_in in string_in:
		try: # find symbols what we can change
			indx = eng_str.index(char_in)
			result_char = ru_str[indx]
			result_string = result_string + result_char
		except: # this symbols not needed to change
			result_string = result_string + char_in
	return result_string

@register("From rus to eng", "e")
def string_from_ru_to_eng(string_in):
	eng_str=u'qwertyuiop[]asdfghjkl;\'zxcvbnm,./`QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>~'
	ru_str =u'йцукенгшщзхъфывапролджэячсмитьбю.ёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
	result_string = ''

	for char_in in string_in:
		try: # find symbols what we can change
			indx = ru_str.index(char_in)
			result_char = eng_str[indx]
			result_string = result_string + result_char
		except: # this symbols not needed to change
			result_string = result_string + char_in
	return result_string
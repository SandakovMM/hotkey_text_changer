# There is a default file to add some string changers functions

# There is a test string function
def string_add_dots(string_in):
	result_string = ''
	for char_in in string_in:
		result_string = result_string + char_in + '.'
	return result_string
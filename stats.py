list = [
'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 
'a', 's', 'd', 'f', 'g', 'h', 'k', 'l', 'z', 'x', 
'c', 'v', 'b', 'n', 'm',]
def num_of_words(string):
	words = string.split()
	return len(words)
def count_characters(string):
	new_string = string.lower()
	dictionary = {}
	for char in list:
		num_of_char = get_amount_of_character(new_string, char)
		dictionary[char] = num_of_char
	return dictionary
def get_amount_of_character(string, letter, num=0):
	for char in string:
		if char == letter:
			num += 1
	return num
def sort_letters(dictionary):
	list_of_dicts = []
	for key in dictionary:
		val = dictionary[key]
		d = {}
		d["char"] = key
		d["num"] = val
		list_of_dicts.append(d)
	list_of_dicts.sort(key=num_key, reverse=True)
	return list_of_dicts
def num_key(dictionary):
	return dictionary["num"]
# {'a': 1000, 'q': 2000, etc.}

from stats import num_of_words
from stats import count_characters
from stats import sort_letters
import sys
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()
def main():
	text = get_book_text(sys.argv[1])
	print("============ BOOKBOT ============")
	print("Analyzing book found at " + sys.argv[1] + "...")
	print("----------- Word Count ----------")
	number = num_of_words(text)
	print("Found " + str(number) + " total words")
	print("--------- Character Count -------")
	dict_list = sort_letters(count_characters(text))
	for entry in dict_list:
		char = entry["char"]
		num = entry["num"]
		print(char + ": " + str(num))
	print("============= END ===============")
main()
# EXIT

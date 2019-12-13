from collections import Counter
def word_count(fname):
	with open(fname) as f:
		return Counter(f.read().split())
print("Number of words in a file:",word_count("text.txt"))
import re
def get_purchase_amount(line):
	matched = re.match('(^[.0-9]+),.*', line)
	if not matched:
			print "Can't be real, bug" 
			return 0
	purchase_amount = matched.group(1)
	return float(purchase_amount)	

def get_creative_id(line):
	matched = re.match(".*user_id=([0-9]+)", line)
	if not matched:
			print "the creative_id is not correct."
			return ""
	creative_id = matched.group(1)
	return creative_id

def main():
	this_file = open("fab_user_purchase.txt")
	import collections
	ddict = collections.defaultdict(float)

	# Using defaultdict to add up the dictionary number based on the creative key
	for line in this_file:
		k = get_creative_id(line)
		v = get_purchase_amount(line)
		ddict[k] += v

	for word in ddict:
		print "{} user generated {} amount of money ".format(word, ddict[word])

if __name__ == "__main__":
	main()

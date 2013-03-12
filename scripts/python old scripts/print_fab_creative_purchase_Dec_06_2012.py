import re
def get_purchase_amount(line):
	matched = re.match('.*amount_to_charge=([.0-9]+);user.*', line)
	if not matched:
			print "!!!!Error regex the purchase amount!!!, this line has problem: \n{}".format(line)
			return 0
	purchase_amount = matched.group(1)
	return float(purchase_amount)	

def get_creative_id(line):
	matched = re.match(".*user_id.*,.*,([0-9a-f]{10}),.*", line)
	if not matched:
			print "*********************** No matching creative"
			return ""
	creative_id = matched.group(1)
	return creative_id

def main():
	this_file = open("fab_creative_purchase.txt")
	import collections
	ddict = collections.defaultdict(float)
	
	# Using defaultdict to add up the dictionary number based on the creative key
	for line in this_file:
		k = get_creative_id(line)
		v = get_purchase_amount(line)
		ddict[k] += v
	
	for word in ddict:
		print "{} creative has generated {} amount of money ".format(word, ddict[word])

if __name__ == "__main__":
	main()

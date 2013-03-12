import re
def get_purchase_amount(line):
	matched = re.match('.*amount_to_charge=([.0-9]+);user.*', line)
	if not matched:
			print "!!!!Error regex the purchase amount!!!, this line has problem: \n{}".format(line)
			return 0
	purchase_amount = matched.group(1)
	return float(purchase_amount)	

def is_iphone(line):
	matched = re.match('.*ios.*', line)
	if matched:
			return True
	else:
			return False

def is_ipad(line):
	matched = re.match('.*ipad.*', line)
	if matched:
			return True
	else: 
			return False

def main():
	sum_iphone = 0
	sum_ipad = 0
	this_file = open("fab_purchase.rtf")

	# Check each line directly, if it's iphone, add to sum_iphone, if it's ipad, add to sum_ipad.
	for line in this_file:
			if is_iphone(line):
					addition = get_purchase_amount(line)
					sum_iphone += addition 
					print 'sum_iphone added this number: {}'.format(addition)
			elif is_ipad(line):
					addition = get_purchase_amount(line)
					sum_ipad += addition 
	
	print "{} is the iphone amount, and {} is the ipad amount. Have a great day.".format(sum_iphone, sum_ipad)

if __name__ == "__main__":
	main()

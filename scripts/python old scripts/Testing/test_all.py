import hashlib
urllib
str = 'testing_purpose'

def get_sha1(str):
	sha1 = hashlib.sha1()
	sha1.update(str)
	return sha1.hexdigest()

str = raw_input('type in a sentence or a letter: ')

str = 'waht do you mean man, i don\'t really get you '
print str[2:22]



import sys

def readfile(filename):
    '''print a file to the standard output. '''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line,
    f.close()



















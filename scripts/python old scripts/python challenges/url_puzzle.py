import urllib

nothing = "8022"
count = 0

while(nothing.isdigit()):
    # Get html using urllib.urlopen
    response = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+nothing)
    html = response.read()

    # After getting nothing part change the nothing value accordingly 
    nothing = html.split(' ')[-1]

    # Closure
    print html
    count += 1

print "there are in total {} numbers.".format(count)


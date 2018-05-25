import webbrowser
#webbrowser.open("http://www.google.com")
print "Hello user. Please enter your date of year"
age =input ()
if age >100:
	print "You are more than 100"
elif age == 100:
	print "Your age is 100"
elif age > 50:
	print "your age is more than 50 but less than 100"
else:
	print "your age is less than 50"
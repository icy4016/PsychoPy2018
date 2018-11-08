formatter = "%r %r %r %r"
formatter1 = "%r\n%r\n%r\n%r\n"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter1 % ( "I had this thing." ,"That you could type up right.", 
"But it didn't sing.", "So I said goodnight.")
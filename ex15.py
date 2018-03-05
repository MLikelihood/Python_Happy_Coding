teststring = "this is a test"
result = teststring.split("t")
print(result)

teststring = "  this      has a lot    of   spaces and    tabs"
result = teststring.split()
print(result)


result = "**".join(result)
print(result)

"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
def readFile(f):
    for line in f:
        print(line)

fooFile = open("foo.txt", "r")
readFile(fooFile)
fooFile.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

# Write:
print() # print empty line

barFile = open("bar.txt", "w")
line = "three lines of arbitrary content\n"
barFile.writelines([line, line, line])
barFile.close()

# Read:
readBarFile = open("bar.txt", "r")
readFile(readBarFile)
readBarFile.close()
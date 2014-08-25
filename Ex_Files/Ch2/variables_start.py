# 
# Example file for variables
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

f = 0;
print f

f = "abc"
print f

def someftn():
    global f
    f = "def"
    print f 
    
    someftn()
    print f 
     
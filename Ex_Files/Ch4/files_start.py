#
# Read and write files using the built-in Python file methods
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main():
    
    f = open("textfile2.txt","r")
    if f.mode == 'r':
        contents = f.read()
        print contents
    
if __name__ == "__main__":
      main()

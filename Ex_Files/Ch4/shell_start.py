#
# Example file for working with filesystem shell methods
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

import os
from os import path

def main():
    print os.name
      
    print "path =" + str(path.realpath("textfile2.txt"))
    
    print "real path = " + str(path.split(path.realpath("textfile.txt")))
    
    
      
if __name__ == "__main__":
  main()
  
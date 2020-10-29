#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
 # f  = open("text.txt" , "w+")
  
  # Open the file for appending text to the end
  # for i in range(10):
  #   f.write("This is line " + str(i) + "\r\n")
    
 # f.close()
  # # write some lines of data to the file
  # f  = open("text.txt" , "a")
  # for i in range(10):
  #   f.write("This is line " + str(i) + "\r\n")
  # # close the file when done
  # f.close()

  # Open the file back up and read the contents
  f  = open("text.txt" , "r")
  if f.mode == 'r':
    # content =  f.read()
      fl = f.readlines()
      for x in fl:
        print(x)
    
if __name__ == "__main__":
  main()

#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  # print(os.name)
  
  # # Check for item existence and type
  # print("Item exists : "+str(path.exists("text.txt")))
  # print("Item exists : "+str(path.isfile("text.txt")))
  # print("Item exists : "+str(path.isdir("text.txt")))
  
  # Work with file paths
  # print("Item path : "+str(path.realpath("text.txt")))
  # print("Item exists : "+str(path.split(path.realpath("text.txt"))))

  
  
  # Get the modification time
  # t = time.ctime(path.getmtime("text.txt"))
  # print(t)
  # print(datetime.datetime.fromtimestamp(path.getmtime("text.txt")))
  
  # Calculate how long ago the item was modified
  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("text.txt"))
  print ("It has been "+str(td) +" Since the file has been modified")
  print("or , " + str(td.total_seconds()) + " Seconds")
  
if __name__ == "__main__":
  main()

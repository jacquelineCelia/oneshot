#!/usr/bin/python
import os
import sys
import string
import codecs
from optparse import OptionParser

def main():
   parser = OptionParser()
   parser.add_option("-l", dest = "l", help = "a list of transcriptions")
   parser.add_option("-n", dest = "n", help = "number of characters")
   (options, args) = parser.parse_args()
   if len(args) != 0:
      parser.error("incorrect number of arguments, please type -h for more help.")
   fin = open(options.l)
   line = fin.readline()
   counter = 0
   while line : 
      counter = counter + 1
      filename = line.strip()
      cmd = "mv ~/timestamps/" + filename + ".1.sec ~/Documents/Research/oneshot/chosen_words/" + options.n + "/" + options.n + "_" + str(counter) + "_1.sec"
      print cmd
      os.system(cmd)
      cmd = "mv ~/timestamps/" + filename + ".2.sec ~/Documents/Research/oneshot/chosen_words/" + options.n + "/" + options.n + "_" + str(counter) + "_2.sec"
      print cmd
      os.system(cmd)
      line = fin.readline()

   fin.close()

if __name__ == "__main__":
   main()

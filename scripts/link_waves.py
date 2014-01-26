#!/usr/bin/python
import os
import sys
import string
import codecs
from optparse import OptionParser

def main():
   parser = OptionParser()
   parser.add_option("-l", dest = "l", help = "a list of wave files to link to")
   parser.add_option("-n", dest = "n", help = "number of characters")
   parser.add_option("-i", dest = "i", help = "1 or 2")
   (options, args) = parser.parse_args()
   if len(args) != 0:
      parser.error("incorrect number of arguments, please type -h for more help.")
   fin = open(options.l)
   line = fin.readline()
   counter = 0
   while line : 
      counter = counter + 1
      filename = line.strip()
      cmd = "ln -s " + filename + " ~/Documents/Research/oneshot/chosen_words/" + options.n + "/" + options.n + "_" + str(counter) + "_" + options.i + ".orig.wav"
      print cmd
      os.system(cmd)
      line = fin.readline()

   fin.close()

if __name__ == "__main__":
   main()


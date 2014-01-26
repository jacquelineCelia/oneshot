#!/usr/bin/python
import os
import sys
import string
import codecs
from optparse import OptionParser

def main():
   tokens = sys.argv[1].split('_')
   print tokens
   tag = "/Users/JackieLee/Documents/Research/oneshot/4_female/" + tokens[0] + "/" + sys.argv[1].strip()
   fsec = open(tag + ".sec")
   t1 = float(fsec.readline().strip())
   t2 = float(fsec.readline().strip())
   fsec.close()
   cmd = "~/Desktop/ffmpeg -ss " + str(t1) + " -t " + str(t2 - t1) + " -i " + tag + ".orig.wav " + tag + ".seg.wav"
   print cmd
   os.system(cmd)
   

if __name__ == "__main__":
   main()


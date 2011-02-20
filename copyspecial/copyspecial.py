#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# Write functions and modify main() to call them
def find_files(dir):
  return [ os.path.abspath(os.path.join(dir, f))
    for f in os.listdir(dir) if re.search(r'__\w+__', f) ]

def copy_files(files, dir):
  if not os.path.exists(dir):
    os.mkdir(dir)
  for filename in files:
    shutil.copy(filename, dir)
  return

def zip_files(files, zip):
  cmd = 'zip -j ' + zip + ' ' + ' '.join(files)
  status, output = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output + '\n')
    sys.exit(1)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # Call your functions
  files = []
  for a in args:
    files += find_files(a)

  if todir:
    copy_files(files, todir)
  elif tozip:
    zip_files(files, tozip)
  else:
    print '\n'.join(files)
  
if __name__ == "__main__":
  main()

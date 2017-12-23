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

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
  filenames = os.listdir(dir)
  paths = []
  for file in filenames:
    special_files = re.search(r'__(\w+)__', file)
    if special_files:
      paths.append(os.path.abspath(os.path.join(dir, file)))
  return paths

def copy_to(paths, dir):
  # Create destination directory
  # If it doesn't exist
  if not os.path.exists(dir):
    os.mkdir(dir)

  for path in paths:
    file = os.path.basename(path)
    if os.path.exists(path):
      shutil.copy(path, os.path.join(dir, file))

def zip_to(paths, zippath):
  paths = ' '.join(paths)
  command = 'zip -j ' + zippath + ' ' + paths
  print "Executing: " + command
  (status, output) = commands.getstatusoutput(command)
  if status:
    sys.stderr.write(output)
    sys.exit(status)
  print output


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

  # +++your code here+++
  # Call your functions
  file_paths = []
  for path in args:
    special_paths = get_special_paths(path)
    file_paths.extend(special_paths)

  if todir:
    copy_to(file_paths, todir)
  if tozip:
    zip_to(file_paths, tozip)

if __name__ == "__main__":
  main()

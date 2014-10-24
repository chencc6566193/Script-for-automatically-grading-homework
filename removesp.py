# @author Xu Yan
# @date Sep.28th,2014
# The python script is used to rename the zip files of the student's submission
# Usage: python removesp.py

import os
import sys
import time
import subprocess
import re
import zipfile
import shutil

executables = ["hw2pr1"]
optional = ["hw2pr4"]



def remove(root,i):
	#newname = re.sub(r'\ \b',r'_',i)#replace ' ' with '_'
	newname = i[-10:]
	newDir = os.path.join(root,newname)
	os.rename(os.path.join(root,i),newDir)
	
def unzip(my_dir,my_zip):
    with zipfile.ZipFile(my_zip) as zip_file:
        for member in zip_file.namelist():
            filename = os.path.basename(member)
            # skip directories
            if not filename:
                continue

            # copy file (taken from zipfile's extract)
            source = zip_file.open(member)
            target = file(os.path.join(my_dir, filename), "wb")
            with source, target:
                shutil.copyfileobj(source, target)

def main():
  """Main entry point for the script"""
  for root, dirs, list in os.walk("/home/congcongchen/Desktop/grader/hw4/2014-10-12-123254"):  
    for i in list:  
      dir = os.path.join(root, i)  
      if i.endswith(".zip"):#unzip the file
        print dir
	try:
        	unzip(root,dir)
	except:#catch all exception
		print "Error"+dir   


  for root, dirs, list in os.walk("/home/congcongchen/Desktop/grader/hw4/2014-10-12-123254"):  
    for i in list:  
      dir = os.path.join(root, i)  
      if i.endswith(".cpp"):#change the name of the file
        remove(root,i)     

if __name__ == '__main__':
  sys.exit(main())

# @author Congcong Chen
# @date Oct.24th,2014

import os
import sys
import time
import subprocess




def runTest(exe,outputFile):
  testFile = exe + "TestFile.txt"
  child = subprocess.Popen(["cat","/home/congcongchen/Desktop/grader/hw4/input.txt"], stdout=subprocess.PIPE)
  child2 = subprocess.Popen([exe], stdin=child.stdout, stdout=subprocess.PIPE)
  
  time.sleep(0.1)

  # Check whether child2 process is still running or not
  if os.path.exists("/proc/" + str(child2.pid)):
    child2.kill()

  # out is a tuple (stdoutdata, stderrdata)
  out = child2.communicate()
  
  if out[1] is not None:
    outputFile.write("Run-time error\n" + out[1])
  else:
    outputFile.write(out[0])
  

def main():
  """Main entry point for the script"""
  for root, dirs, list in os.walk("/home/congcongchen/Desktop/grader/hw4/2014-10-12-123254"):   
    for i in list:  
      dir = os.path.join(root, i)      
      if i=="3":
	outputFile = open(os.path.join(root, "result.txt"),"w") 
	try:
		runTest(dir,outputFile)
	except:
		print "Exception"
      

if __name__ == '__main__':
  sys.exit(main())

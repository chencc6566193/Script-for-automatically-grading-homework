Script-for-automatically-grading-homework
=========================================

This script is used to automatically run students' homework and output results into .txt file.

How to use (this program is test under Unbuntu 14.04):
a. run removesp.py
b. run g.sh
c. run running.py

1. removesp.py is used to traverse the directories and then unzip and extract .cpp files from .zip file. And for each .cpp file, it will cut .cpp file's name and leave the last 10 characters.

2. g.sh file will automatically visit every .cpp file and compile .cpp file into .exe file. 

3. running.py will automatically run each .exe file read input from input.txt file and write output to result.txt

Note: You should provide input.txt file.

# !/bin/sh
# Grading Shell Script for ENGR112 HWs
# Functionalities: unzip submissions in UIN folders and compile cpp files in the folders
# @author XuYan
# @date Sep.28th,2014

function unzip_compile() {
  SOURCEFILES=("hw4pr1.cpp" "hw4pr2.cpp" "hw4pr3.cpp" "hw4pr4.cpp")
  DEPENDENCY=("std_lib_facilities_4.h" "running.py")
  TESTFILES=("hw4pr1TestFile.txt" "hw4pr2TestFile.txt" "hw4pr3TestFile.txt" "hw4pr4TestFile.txt")
  currentDirectory=$(pwd)
  
  for folder in */; do
	# move header file into UIN folders
	for dependencyFile in "${DEPENDENCY[@]}"
	do
		if [ ! -f $folder/$dependencyFile ]
		then
			cp $dependencyFile $folder
		fi
	done
	
	cd $folder
    for z in *.zip
    do
		if [ ! -f ${SOURCEFILES[0]} ]
		then
			unzip $z
		fi
		compile
		#run $1 $2 $3
	done
	
	cd $currentDirectory
  done
}

function compile() {
  g++ -std=c++11 ${SOURCEFILES[0]} -o 1
  g++ -std=c++11 ${SOURCEFILES[1]} -o 2
  g++ -std=c++11 ${SOURCEFILES[2]} -o 3

  if [ -f ${SOURCEFILES[3]} ]
  then
    g++ -std=c++11 ${SOURCEFILES[3]} -o 4
  fi
}

function run() {
  echo "----------pr1 output----------" >> Result.txt
  ./hw2pr1 < $1 >> Result.txt

  echo "----------pr2 output----------" >> Result.txt
  # For single execution program
  #while read input
  #do
    #echo "$input" | ./hw2pr2 >> Result.txt
  #done < "$1"
  
  # For repeated execution program
  ./hw2pr2 < $1 >> Result.txt

  echo "----------pr3 output----------" >> Result.txt
  # For single execution program
  #cat $2 | while read input
  #do
    #echo $input | ./hw3pr3 >> Result.txt
  #done
  
  # For repeated execution program
  ./hw2pr3 < $2 >> Result.txt

  if [ -f hw1pr4.cpp ]
  then
    echo "----------pr4 output----------" >> Result.txt
    ./hw2pr4 < $3 >> Result.txt
  fi
}

# Starting point of the shell script

if [ $# -ne 0 ]
  then
    "Usage: ./gradingScript"
    exit 1
fi

#if [ ! -f $1 -o ! -f $2 -o ! -f $3]
#  then
#    "$1, $2 or $3 was not found in directory"
#    exit 1
#fi

unzip_compile $1 $2 $3

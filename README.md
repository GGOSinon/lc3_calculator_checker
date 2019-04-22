# lc3_calculator_checker

Python code which checks your calculator project.



## Requirements

- Python3
- LC-3 simulator(./lc3sim)

## Usage

To use this project, you must have your obj file(calc.obj) in your lc3 folder.

First change your directory to ~/lc3.
	
	std00000@ccp0:~$ cd lc3
	
And copy this project with command below.

	std00000@ccp0:~/lc3$ git clone https://github.com/GGOSinon/lc3_calculator_checker.git

Copy the python file in the lc3 folder.

	std00000@ccp0:~/lc3$ cd lc3_calculator_checker
	std00000@ccp0:~/lc3/lc3_calculator_checker$ cp checker.py ../
	
And execute this code.

	std00000@ccp0:~/lc3/lc3_calculator_checker$ cd ..
	std00000@ccp0:~/lc3$ python3 checker.py

## Details
This code will test your code with 8596 test cases consist of:

- All cases for numbers in [-16, 15] (32*32*3 + 32*16*2 = 4096 test cases, since / and % doesn't have negative divisor.)
- Random cases(5000 test cases)
- Delete some of the cases to make output stable(delete 500 cases)

If the program has correct answer you'll see the output like:

	Case 50 : YES 12+5=17

If the program has incorrect answer you'll see the output like:

	NO answer is 15
	3*5=13

It means that your program gave a incorrect answer 13 for the test case 3*5, which the correct answer is 15.

<h1>Project 5 - Simulation of Page Replacement Strategies </h1>
  by: Xander Palermo

<h2>Background </h2>
This program is coded using python.

In my solution for this project, I created a main function located within simpager.py.

The main function will open an input file, format the input into an Std_Input container, and then send it to a class called Algorithms, that performs the inputted algoritms on the input data


<h2>Required Files </h2>
Place simpager.py, replacement_algorithms.py, std_input.py, file_handler.py and an input file into the same directory (preferably on the lovelace server)

(you can also you the git clone command for this repository, and that will load all the files necessary)

> git clone https://github.com/aPalermooo/CSC360-Project5.Page-Replacement-Strategies/

A sample input file is included

<h3>Input File Formatting:</h3>

> reference string of pages (seperated by ' ')
>
> Number of Frames available to the simulations
>
> Mnemonic of desired algorithm (can be multiple, sepereated by new lines)
>
>  ...
>

<h2>Running the program</h2>
The following command will print results of the simulations

> python3 simpager.py
>


The program defaults to searching for p52.txt when no parameters are given


However the program can take attributes to read a different file, if desired

> python3 simpager.py p52.txt
> 
> python3 simpager.py other_input_file_example.txt

..and so on

<h2>Checking output</h2>
All output of the program is printed to console

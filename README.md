# Project 1, Pendulum Simulation
## Grant Smith & Patrick Wright


### data_logging_script_microbit.py

The data collection code is found by running the file 'data_logging_script_microbit.py'
Press the A button to start data collection then press the A button once more to end the data collection.
This will return a file named 'csvfile.txt' into your microbit and then drag and drop from microbit into your computer.

### simulation_code.py

For simulation code run 'simulation_code.py' 
This will produce three graphs one with velocity vs. time another with position vs. time and a final of acceleration vs. time.
It will print the results at given the given time step and display time, velocity, acceleration, and position.
A .csv file will be output to the current directory with time in milliseconds and acceleration in milli-gs.
Variables that should be updated depedning on the test are:
'test_number' this will put the number of the test in the name of the csv file
'length' this is the length of the pendulum arm
'timeinitial' this is if you want the simulation to start at another time than 0
'timestep' this is the size of time step for the simulation
'mangle' this is the maximum angle of the pendulum (the starting angle)



### data_analysis.py

'data_analysis.py' will calculate the period after parsing the data and filtering it.
Variables that should be updated depedning on the test are:
'file' this is the path of the file that should be run in the analysis program
'Length' this is the length of the pendulum used and is only used in nameing the graph
'testnumber' this is the number of the test used in naming the graph
'realorsim' this is if the test is real world data or simulation data and is used in naming the graphs

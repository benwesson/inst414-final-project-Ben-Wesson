# inst414-final-project-Ben-Wesson
pip install -r /path/to/requirements.txt

Project Overview
1.Business problem: Maryland blue crab population fluctuates year to year causing hikes in crab prices and shortages. Maryland blue crab population has been in decline since the 1990s. Comapre the crab populations other states to explore possible solutions.

2.Data sets used: Stock Assessment of the North Carolina Blue Crab, Chesapeake Bay Blue Crab Advisory Report

3.techniques employed: Measuring crab population stability between states by measuring percent change in popualtion counts year to year 

4.expected outputs 1 line graph per call of lineGraph function

Setup Instructions
1.Clone github repo https://github.com/benwesson/inst414-final-project-Ben-Wesson/tree/main in Vs code.

2.Set up virtual enviroment. To do this open terminal. The enter this command python -m venv [environment name]. Then this command source [environment name]/bin/activate. Then choose a file to store your data. 

3.Run the requirments.txt file in the setup folder. Open the terminal and run this command pip install -r setup/requirements.txt  

Running the Project
1.Follow the logic in main.py. Choose a state to examine. Then get the graph and cleaned file that corresponds to your chosen state. MD for maryland and nc for north carolina. 

2.Ingest CSVs as dataframes.

3.Get the year column from the cleaned file and the crab column from the graph file.

4.Call the graph function. Use years as x axis and crabs as y axis.

Code Package Structure
1. 6 sections of code.

2. Data folder stores dataset CSVs

3. elt flolder stores data cleaning scripts

4. analysis folder stores scripts that run stastical models on data sets

5. visuals folder has scripts to plot datasets

6. setup folder has requirments.txt which must be run after setting up your virtual environment to ensure package works


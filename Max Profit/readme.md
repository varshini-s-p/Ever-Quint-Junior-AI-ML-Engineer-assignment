# Max Profit Problem – EverQuint Assignment

## Overview
This project solves the Max Profit Problem as described in the EverQuint / HCL GUVI assessment.
The objective is to determine the optimal mix of properties (Theatre, Pub, Commercial Park)
that maximizes total earnings within a given number of time units.

The solution strictly follows all constraints mentioned in the problem statement:
- Only one property can be developed at a time
- Earnings start after construction completion
- Earnings accumulate per remaining unit of time

## Project Structure
- max_profit.py : Command-line solution
- max_profit_logic.py : Core algorithm logic
- app.py : Streamlit web application
- requirements.txt : Project dependencies

## Running the Solution

### Command Line
python max_profit.py

### Streamlit Application
streamlit run app.py

## Deployment
The Streamlit application has been deployed successfully.
The deployment URL is shared as part of the submission.

## Algorithm
The problem is solved using Dynamic Programming based on time units.
The algorithm evaluates all possible construction sequences and selects the combination
that maximizes total earnings.

## Validation
The solution has been tested with all sample inputs provided in the PDF (n = 7, 8, 13),
and the outputs match the expected results exactly.

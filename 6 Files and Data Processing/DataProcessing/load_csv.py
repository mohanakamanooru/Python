# Concept produced by Saul Johnson <saul.johnson@tees.ac.uk>
# Example by James Fairbairn <j.fairabairn@tees.ac.uk>
# We wrote this together in class.
#
# **DO NOT REMOVE THIS HEADER**
#
# Notes:
#   + This file is for demonstration purposes only.
#   + You must use this example to guide your own solution.
#     **DO NOT SUBMIT THIS FILE FOR ASSESSMENT**

# Import Pandas so we can work with CSV files.
import pandas as pd

# Load CSV file into data frame.
df = pd.read_csv("weight-height-data.csv")

# Create variables for number of rows and total height of all people added together.
total_num_rows = 0
total_height = 0

# Loop over rows in data frame.
for i, row in df.iterrows():
    total_height += row["Height"] # Add height total.
    total_num_rows += 1 # Increment row count.

# Print number of rows and average height.
print("There are", total_num_rows, "rows in this file")
print("Average height:", total_height / total_num_rows)

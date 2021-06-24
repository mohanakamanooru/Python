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

# Calculate weight/height ratios.
whrs = []
for i, row in df.iterrows():
    whrs.append(row["Weight"] / row["Height"])

# Add weight-height ratio as a column.
df["WHR"] = whrs

# Output into another CSV file.
df.to_csv("processed-output.csv")

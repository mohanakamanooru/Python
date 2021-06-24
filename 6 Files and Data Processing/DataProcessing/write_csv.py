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

import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file into data frame.
df = pd.read_csv("weight-height-data.csv")

# Calculate weight/height ratios.
whrs = []
for i, row in df.iterrows():
    whrs.append(row["Weight"] / row["Height"])

# Add weight-height ratio as a column.
df["WHR"] = whrs

# Output into another CSV file.
df.to_csv("whr-data.csv", index=False)

plt.scatter(df["Weight"],df["Height"])
plt.show()
plt.scatter(df["Weight"],df["WHR"])
plt.show()
plt.scatter(df["Height"],df["WHR"])
plt.show()

    

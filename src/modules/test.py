from ginee_reader import extract_from_ginee
from output_generator import generate_sales_import
import pandas as pd
import numpy as np

# test files
ginee_file_dir = "../temp/GINEE-LAZADA_JABRA.xlsx"
df = extract_from_ginee(ginee_file_dir)

# print(df)
generate_sales_import(df["output"], 20,  "../temp/")

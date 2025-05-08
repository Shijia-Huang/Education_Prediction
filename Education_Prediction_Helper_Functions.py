import re
import numpy as np
def extract_parentheses_content(text):
    # Use regular expression to find all content inside parentheses
    if type(text) == str:
        label = re.search(r'\((.*?)\)', text)
        if label != None:
            # content = re.findall
            (r'\((.*?)\)', text)
            return float(label.group(1))
    return text

def is_negative(x):
    try:
        return np.NaN if float(x) <0 else x
    except:
        return x

def is_empty(x):
    if type(x) == str:
        if len(x.strip()) == 0:
            return np.NaN
    return x

def encoding(x):
    if type(x) == str:
        if "-1" in x or "-2" in x or "-3" in x or "-4" in x or "-5" in x or "-6" in x or "-7" in x or "-8" in x or "-9" in x or "nan" in x.lower() or "na" in x.lower():
            return np.NaN 
    return 
    
def find_columns_with_number_dash_number(df):

    pattern = r'^\d+\s*[-:]\s*\d+$'
    
    # List to store column names that match the age equivalence pattern
    matching_columns = []
    
    # Iterate over all columns in the DataFrame
    for column in df.columns:
        if df[column].astype(str).apply(lambda x: bool(re.match(pattern, x))).any():
            matching_columns.append(column)
    
    return matching_columns

def round_text(x):
    if type(x) == str:
        if "<" in x:
            return float(x.split("<")[1]) * 0.9
        elif ">" in x:
            return float(x.split(">")[1]) * 1.1
        else: 
            return x
    else:
        return x

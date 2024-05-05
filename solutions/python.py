import pandas as pd
import os
import re
import random
import string

"""
Let's have a string generator (`generator()`) that returns random strings like `435-d3D.ss345`. We
need to write 3 filtering (lambda) functions, that would filter the generated output for:
"""

def generator():
    """
    A prototype generator function for genrating random stringss
    """
    random_string = ''.join(random.choices(string.digits + string.ascii_letters, k=3))
    random_number = ''.join(random.choices(string.digits, k=3))
    random_extension = ''.join(random.choices(string.ascii_lowercase, k=3))
    return f"{random_string}-{random_number}.{random_extension}"


for _ in range(5):
    generated_string = generator()

    extract_integers = lambda s: ''.join(re.findall(r'\d+', s)) if re.findall(r'\d+', s) else None # only integers
    extract_integers(generated_string)
    extrac_json_csv = lambda s: s if s.endswith(('.json', '.csv')) else None #those ending with ".json" or ".csv"
    extrac_json_csv(generated_string)
    extract_dates = lambda s: ''.join(re.findall(r'\b\d{4}-\d{2}-\d{2}\b', s)) if re.findall(r'\b\d{4}-\d{2}-\d{2}\b', s) else None# dates in ISO format (2019-05-27)
    extract_dates(generated_string)

"""
or we can create a list of random strings manualy for testing purposes
"""
strings = ['ddT-034.jho',
'MKN-xyc.csv',
'CE6-647.aqf',
'JZG-(2019-05-27.whh',
'Xjg-292.yfm']

extract_integers = lambda s: ''.join(re.findall(r'\d+', s)) if re.findall(r'\d+', s) else None # only integers
filtered_integers = [extract_integers(string) for string in strings if extract_integers(string) is not None]
print('------------------------------------------')
print(f'integers from strings list {filtered_integers}')

extrac_json_csv = lambda s: s if s.endswith(('.json', '.csv')) else None #those ending with ".json" or ".csv"
filtered_extrac_json_csv = [extrac_json_csv(string) for string in strings if extrac_json_csv(string) is not None]
print(f'strings ending with json or csv {filtered_extrac_json_csv}')

extract_dates = lambda s: ''.join(re.findall(r'\b\d{4}-\d{2}-\d{2}\b', s)) if re.findall(r'\b\d{4}-\d{2}-\d{2}\b', s) else None# dates in ISO format (2019-05-27)
filtered_extrac_dates = [extract_dates(string) for string in strings if extract_dates(string) is not None]
print(f'dates in ISO format from strings {filtered_extrac_dates}')






"""
Let's have a folder with an unspecified number of CSV files that have various sizes. For each file we
need to calculate a sum of a column in relation to another column (e.x. `sum(a) where b = 'foo'`).
"""

def calculate_sum(folder_path, column_to_sum, filter_column, filter_value):
    """
    Calculate the sum of a specific column in CSV files within a folder based on a filter condition.

    Parameters:
    - folder_path (str): The path to the folder containing the CSV files.
    - column_to_sum (str): The name of the column whose sum is to be calculated.
    - filter_column (str): The name of the column on which to apply the filter.
    - filter_value: The value to filter the 'filter_column' by.

    Returns:
    - pandas.DataFrame: A DataFrame containing the filenames, the filter column name, the column to sum,
      and the sum of the specified column based on the filter condition.
    """
   
    columns = ['filename', 'filter_column', 'column_to_sum', 'column_sum']
    result_df = pd.DataFrame(columns=columns)    

    for filename in os.listdir(folder_path):
        summary = []
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)
            column_sum = df.loc[df[filter_column] == filter_value][column_to_sum].sum()
            summary.extend([filename, filter_column, column_to_sum, column_sum])
            result_df.loc[len(result_df)] = summary
    return result_df


folder_path = os.getcwd()
column_to_sum = 'col2'
filter_column = 'col1'
filter_value = 'car'
result = calculate_sum(folder_path, column_to_sum, filter_column, filter_value)
print('------------------------------------------')
print(result)


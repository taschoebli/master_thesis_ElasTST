import pandas as pd

# Load your CSV file (update 'input_file.csv' with your file path)
input_file = '/Users/schoebl/Downloads/power_with_sunrise_set.csv'
output_file = '/Users/schoebl/Downloads/240710_250110_power_with_sunrise_set.csv'

# Read the CSV file with ';' as delimiter
data = pd.read_csv(input_file, delimiter=';')

# Adjust the 'validdate' column format
data['validdate'] = pd.to_datetime(data['validdate']).dt.strftime('%Y-%m-%d %H:%M:%S')

# Save the updated file with ',' as the delimiter
data.to_csv(output_file, index=False, sep=',')

print(f"File saved successfully at: {output_file}")

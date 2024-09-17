import os
import pandas as pd

folder_path = os.getcwd()  
merged_file = "output.txt"

# Opening the output file
with open(merged_file, 'w') as outfile:
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            # Read the CSV file            
            df = pd.read_csv(filename)
            df.columns = df.columns.str.strip() 
            print(f"Columns in {filename}: {df.columns}") 
            if 'SHORT-TEXT' in df.columns:
                text_column = df['SHORT-TEXT']
            elif 'TEXT' in df.columns:
                text_column = df['TEXT']
            else:
                print(f"No 'TEXT' or 'SHORT-TEXT' column found in {filename}")
                continue 
            for line in text_column:
                outfile.write(line + '\n')        
print(f"Text extracted and saved to {merged_file}")


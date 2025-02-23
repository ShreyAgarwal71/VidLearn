import os
import csv
import pandas as pd

# Define the folder containing CSV files
folder_path = '/Users/home/Documents/Programs/VidLearn/static/csv_reviews'
output_file = '/Users/home/Documents/Programs/VidLearn/static/csv_reviews/master.csv'

# Initialize a list to store summary data
summary_data = []

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
   
    # Check if the file is a CSV
    if filename.endswith('.csv'):
        try:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)
           
            # Calculate required metrics
            total_score = df['Score'].sum()
            scores_above_80 = df[df['Score'] >= 80].shape[0]
            scores_65_to_79 = df[(df['Score'] >= 65) & (df['Score'] < 80)].shape[0]
            scores_below_80 = df[df['Score'] < 80].shape[0]
            avg_price = df['Price'].mean()
            avg_design = df['Design'].mean()
           
            # Append results to summary data
            summary_data.append([
                filename, total_score, scores_above_80, scores_65_to_79,
                scores_below_80, avg_price, avg_design
            ])
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Create a DataFrame for the master CSV
columns = [
    'Filename', 'Total Score', 'Scores >= 80', 'Scores 65-79',
    'Scores < 80', 'Average Price', 'Average Design'
]
master_df = pd.DataFrame(summary_data, columns=columns)

# Save the master CSV
master_df.to_csv(output_file, index=False)
print(f"Master CSV saved as {output_file}")
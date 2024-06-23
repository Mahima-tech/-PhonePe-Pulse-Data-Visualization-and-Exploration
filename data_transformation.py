import os
import pandas as pd

clone_dir = 'phonepe_pulse_data'
output_file = 'transformed_data.csv'

def load_and_transform_data():
    data_files = [os.path.join(clone_dir, file) for file in os.listdir(clone_dir) if file.endswith('.csv')]
    
    dataframes = []
    for file in data_files:
        df = pd.read_csv(file)
        dataframes.append(df)
    
    data = pd.concat(dataframes, ignore_index=True)
    
    # Perform necessary cleaning and transformation
    data.dropna(inplace=True)
    
    # Add latitude and longitude columns for example purposes
    if 'latitude' not in data.columns:
        data['latitude'] = 12.9716  # Example latitude value
    if 'longitude' not in data.columns:
        data['longitude'] = 77.5946  # Example longitude value
    
    data.to_csv(output_file, index=False)
    print(f'Data transformed and saved to {output_file}')

if __name__ == "__main__":
    load_and_transform_data()

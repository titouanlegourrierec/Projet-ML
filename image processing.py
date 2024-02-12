import os
import pandas as pd

# Define the directory paths
normal_dir = 'chest_xray/train/NORMAL'
pneumonia_dir = 'chest_xray/train/PNEUMONIA'

# Get the list of all files in each directory
normal_files = [os.path.join(normal_dir, file) for file in os.listdir(normal_dir)]
pneumonia_files = [os.path.join(pneumonia_dir, file) for file in os.listdir(pneumonia_dir)]

# Create a DataFrame
df = pd.DataFrame({
    'file': normal_files + pneumonia_files,
    'label': ['normal'] * len(normal_files) + ['pneumonia'] * len(pneumonia_files)
})

print(df)

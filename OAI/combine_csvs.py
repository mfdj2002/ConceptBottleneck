import pandas as pd
import sys
import os
# Assume you have multiple DataFrames: df1, df2, df3, ...

def main(path):
    # Create a list to store the DataFrames
    for split in os.listdir(path):
        dfs = []
        split_path = os.path.join(path, split)
        if os.path.isdir(split_path):
            for file in os.listdir(split_path):
                if file.endswith('.csv') and file != '.DS_Store':
                    file_path = os.path.join(split_path, file)
                    df = pd.read_csv(file_path)
                    dfs.append(df)

        if len(dfs) == 0:
            continue

        # Concatenate the DataFrames vertically
        combined_df = pd.concat(dfs)

        # Set the 'image_number' column as the index of the combined DataFrame
        combined_df.set_index('image_number', inplace=True)

        # Create a new DataFrame with the desired index
        new_df = pd.DataFrame(index=combined_df.index)
        print(f"saving to {os.path.join(path, split, 'combined.csv')}")
        new_df.to_csv(os.path.join(path, split, 'combined.csv'))


if __name__ == '__main__':
    path = sys.argv[1]
    main(path)
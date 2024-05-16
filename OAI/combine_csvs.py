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


        # Combine the DataFrames vertically
        df_combined = pd.concat(dfs, ignore_index=True)

        # Sort the combined dataframe by 'col1'
        result_df = df_combined.sort_values('image_number')

        # Reset the index
        result_df = result_df.reset_index(drop=True)

        # Explode the 'col' column to separate the values
        # df_combined = df_combined.explode('image_number')

        # # Convert the 'col' column to numeric type
        # df_combined['image_number'] = pd.to_numeric(df_combined['image_number'])

        # # Sort the combined DataFrame based on the 'col' column
        # df_sorted = df_combined.sort_values('image_number')

        # Reset the index
        # df_sorted = df_sorted.reset_index(drop=True)

        # Concatenate the DataFrames vertically
        # combined_df = pd.concat(dfs)

        # # Set the 'image_number' column as the index of the combined DataFrame
        # combined_df.set_index('image_number', inplace=True)

        # # Create a new DataFrame with the desired index
        # new_df = pd.DataFrame(index=combined_df.index)
        print(f"saving to {os.path.join(path, split, 'combined.csv')}")
        result_df.to_csv(os.path.join(path, split, 'combined.csv'))


if __name__ == '__main__':
    path = sys.argv[1]
    main(path)
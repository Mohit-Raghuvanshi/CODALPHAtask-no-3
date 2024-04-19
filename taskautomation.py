import pandas as pd

def sort_csv(input_file, output_file, sort_column):
    try:
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(input_file)
        
        # Check if the specified column exists in the DataFrame
        if sort_column not in df.columns:
            raise ValueError(f"Column '{sort_column}' not found in the CSV file.")
        
        # Sort the DataFrame by the specified column
        df_sorted = df.sort_values(by=sort_column)
        
        # Save the sorted data to a new CSV file
        df_sorted.to_csv(output_file, index=False)
        
        print(f"CSV file '{input_file}' sorted by column '{sort_column}'.")
        print(f"Sorted data saved to '{output_file}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
input_data_file = r'C:\Users\mahim\Downloads\titanic.csv'  # Update with your CSV file path
output_sorted_file = r'C:\Users\mahim\OneDrive\Desktop\outputtitanic.csv'  # Specify the output sorted CSV file path
sort_column = 'Pclass'  # Specify the column by which to sort

sort_csv(input_data_file, output_sorted_file, sort_column)

# This code is to download and offer several 
# functions to specify the data to download.
import pandas
from os import path

def load_data(filename:str, data_dir:str="data"):
    """loaddata loads the data from filename into memory from data_dir data directory."""
    file_path = path.join(data_dir, filename)
    try:
        print(f"Loading data from {file_path}")
        return pandas.read_csv(file_path)
    except:
        print("The file could not be loaded.")

# test function to make sure functions work. 
# this can be changed later
def main():
    filename = "split-prices.csv"
    data = load_data(filename)
    print(data)

if __name__ == '__main__':
    main()

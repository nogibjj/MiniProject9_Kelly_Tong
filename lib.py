import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import numpy as np

def desc_stats(data):  
    # Convert the dataset to a Pandas DataFrame
    Auto = pd.DataFrame(data)

    # Display a brief summary of the dataset
    print(Auto.info())

    # Glimpse the first few rows of the dataset
    print(Auto.head())

    # Summary of the numeric variables
    print(Auto.describe())
    
    return None

def box_visual(data):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        sns.set_theme(style="ticks", palette="pastel")
        sns.boxplot(x="mpg", y="weight", palette="Blues", data=data)
        plt.show()

def main():
    path = "https://raw.githubusercontent.com/nogibjj/MiniProject9_Kelly_Tong/main/test_Auto.csv"
    df = pd.read_csv(path)
    print(desc_stats(df))
    box_visual(df)


if __name__ == "__main__":
    main()

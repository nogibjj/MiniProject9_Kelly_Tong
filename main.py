from lib import desc_stats, box_visual
import pandas as pd

def main():
    path = (
        "https://raw.githubusercontent.com/nogibjj/MiniProject9_Kelly_Tong/main/test_Auto.csv"
    )
    df = pd.read_csv(path)
    sum_data = desc_stats(df)

    print(sum_data)
    box_visual(df)

def data(dataset):
    result = pd.read_csv(dataset)
    return result


if __name__ == "__main__":
    main()

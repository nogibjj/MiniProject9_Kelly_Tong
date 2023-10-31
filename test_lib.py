from lib import desc_stats, box_visual
import pandas as pd


def test_desc_stats():
    path = "https://raw.githubusercontent.com/nogibjj/MiniProject9_Kelly_Tong/main/test_Auto.csv"
    my_df = pd.read_csv(path)
    summary = desc_stats(my_df)
    return summary

def test_box_visuak():
    path = (
        "https://raw.githubusercontent.com/nogibjj/MiniProject9_Kelly_Tong/main/test_Auto.csv"
    )
    df = pd.read_csv(path)
    try:
        box_visual(df)
    except Exception as e:
        assert False, f"data_visual function raised an exception: {e}"

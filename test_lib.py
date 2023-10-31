from lib import desc_stats, box_visual
import pandas as pd


def test_desc_stats():
    path = "https://raw.githubusercontent.com/nogibjj/MiniProject9_Kelly_Tong/main/test_Auto.csv"
    my_df = pd.read_csv(path, sep=";")
    summary = desc_stats(my_df)
    mean = my_df["weight"].mean()
    median = my_df["weight"].median()
    assert mean == summary.loc["mean", "Weight"], "Mean test failed"
    assert median == summary.loc["50%", "Weight"], "Median test failed"

def test_box_visuak():
    data_path = (
        "https://raw.githubusercontent.com/nogibjj/MiniProject9_Kelly_Tong/main/test_Auto.csv"
    )
    df = pd.read_csv(path, sep=";")
    try:
        box_visual(df)
    except Exception as e:
        assert False, f"data_visual function raised an exception: {e}"

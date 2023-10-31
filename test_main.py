import os
import main

def test_data():
  dataset = "test_Auto.csv"
  result = main.data(dataset)
  assert result is not None

def test_box_visual():
  assert os.path.exists("visual.png")

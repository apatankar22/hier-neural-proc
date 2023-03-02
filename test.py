import numpy as np


data_path = "sir_np/test_data/test.npz"

data = np.load(data_path)
conv_data = dict()
conv_data["x"] = data["x"]


print("Sample Data shape:", conv_data["x"].shape)
print("Test runs successfully!")


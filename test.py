import numpy as np



x_path = "../data/test_data/inputs_2003_01_01-00.npy"
y_path = "../data/test_data/outputs_2003_01_01-00.npy"

x = np.load(x_path)
y = np.load(y_path)

print("Sample X shape:", x.shape)
print("Sample Y shape:", y.shape)

print("Test runs successfully!")

print("Future works: integrate active learning with SFNP and MFNP.")

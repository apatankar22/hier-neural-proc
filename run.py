import sys
import numpy as np

def main(targets):
    if 'test' in targets:
        data_path = "data/test-data.npz"
    
    else:
        print("add the test target next time!")
        exit()

    data = np.load(data_path)
    conv_data = dict()

    for i in data:
        conv_data[i] = data[i]

    #print("Sample Data shape:", conv_data)
    print("Sample a shape:", conv_data["a"].shape)
    print("Sample b shape:", conv_data["b"].shape)
    print("Test runs successfully!")

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)

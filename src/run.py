import sys
import numpy as np
import sir_np.helper

def main(targets):
    if 'test' in targets:
        tester = True
        data_path = "../data/test-data.npz"
    
    else:
        print("add the test target next time!")
        exit()

    data = np.load(data_path)
    conv_data = dict()

    for i in data:
        conv_data[i] = data[i]

    #print("Sample Data shape:", conv_data)
    print("Sample a shape:", conv_data["a"].shape)
    print(conv_data["a"][1])
    print("Sample b shape:", conv_data["b"].shape)

    #s1 = Supervisor(tester)
    for i in range((conv_data["a"].shape)[0]):
        x1 = int(conv_data["a"][i])
        x2 = int(conv_data["b"][i])
        print(sir_np.helper.help_run(x1, x2, i))

    print("Test runs successfully!")

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)

import numpy as np


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = x / np.max(x)
    return e_x



if __name__ == "__main__":
    scores = [3.0, 1.0, 0.2]
    print(softmax(scores))
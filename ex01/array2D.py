import numpy as np 

def slice_me(family: list, start: int, end: int) -> list:

    if not isinstance(family, list) or not all(isinstance(row,list) for row in family):
        raise ValueError("Bad arguments: input must be 2D arr")
    if len(set(len(row) for row in family)) != 1:
        raise ValueError("Bad argunments: all row must be same length")
    
    arr = np.array(family)
    print("my shape is :", arr.shape)

    new_arr = arr[start:end]
    print("my new shape is :", new_arr.shape)

    return new_arr.tolist()

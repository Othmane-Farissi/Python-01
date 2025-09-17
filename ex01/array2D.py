import sys
import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D list (matrix-like structure) between given start and
    end indices.

    - Validates that the input is a list of lists (convertible to a
      NumPy array).
    - Prints the original shape and the new shape after slicing.
    - Returns the sliced portion as a standard Python list.

    Args:
        family (list): A 2D list (e.g., list of lists) to slice.
        start (int): The starting index for slicing (inclusive).
        end (int): The ending index for slicing (exclusive).

    Returns:
        list: The sliced portion of the original list.
    """
    try:
        if not isinstance(family, list):
            raise AssertionError("bad arguments")
        elif not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("bad arguments")

        arr = np.array(family)
        print(f"my shape is :  {arr.shape}")

        new = arr[start:end]
        print(f"my new shape is :  {new.shape}")

        return new.tolist()

    except AssertionError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

# tester.py:

# from array2D import slice_me
# family = [[1.80, 78.4],
# [2.15, 102.7],
# [2.10, 98.5],
# [1.88, 75.2]]
# print(slice_me(family, 0, 2))
# print(slice_me(family, 1, -2))

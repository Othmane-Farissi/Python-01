from PIL import Image, UnidentifiedImageError
import numpy as np
import sys


def ft_load(path: str):
    """
    Load an image from the given path and convert it to a NumPy array.

    - Supports only JPEG or JPG images.
    - Prints the shape of the loaded image.
    - Exits the program with an error message if the file is not found,
      is not a valid image, or has an unsupported format.

    Args:
        path (str): The file path to the image.

    Returns:
        np.ndarray: A NumPy array representing the image.
    """
    try:
        im = Image.open(path)
        if im.format not in ("JPEG", "JPG"):
            raise ValueError("Format must be JPEG or JPG")

        imgArr = np.array(im)
        print(f"The shape of image is: {imgArr.shape}")
        return imgArr

    except FileNotFoundError:
        print(f"Error: File '{path}' not found")
        sys.exit(1)
    except UnidentifiedImageError:
        print(f"Error: File '{path}' is not a valid image")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

# tester.py:

# from load_image import ft_load
# import numpy as np
# imgArr = ft_load("landscape.jpg")
# np.set_printoptions(edgeitems=3, threshold=4)
# print(imgArr[:1])
# print(imgArr[-1:])

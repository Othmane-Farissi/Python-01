from PIL import Image, UnidentifiedImageError
import numpy as np

def ft_load(path: str):
    """
    Loads a JPEG/JPG image, prints its shape and pixel RGB values,
    and returns the image as a NumPy array.
    """
    try:
        # Open the image
        im = Image.open(path)
        
        # Check format
        if im.format not in ("JPEG", "JPG"):
            raise ValueError("Format must be JPEG or JPG")
        
        # Convert to NumPy array
        imgArr = np.array(im)
        
        # Print shape
        print("The shape of image is:", imgArr.shape)
        
        # Print first 3 and last 3 rows of pixels
        print(imgArr[:3])
        print(imgArr[-3:])
        
        # Return the array
        return imgArr

    except FileNotFoundError:
        print(f"Error: File '{path}' not found")
        return None
    except UnidentifiedImageError:
        print(f"Error: File '{path}' is not a valid image")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None

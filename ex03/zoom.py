from PIL import Image, UnidentifiedImageError
import numpy as np

def ft_load(path: str):

    try:
        
        im = Image.open(path)
        
        if im.format not in ("JPEG", "JPG"):
            raise ValueError("Format must be JPEG or JPG")
        
        imgArr = np.array(im)
        
        print("The shape of image is:", imgArr.shape)
        
        print(imgArr[:3])
        print(imgArr[-3:])
        
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

def zoom(arr):

    zomed =  arr[:400, :400]

    zomed_one_channel = [:, :, 0]

    print("New shape after slicing: ", zoomed_one_channel.shape)
    print(zomed_one_channel[:3])
    print(zomed_one_channel[-3:])
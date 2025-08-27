from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def ft_zoom(path: str):
    try:
        im = Image.open(path)

        # Ensure format is JPEG/JPG
        if im.format not in ["JPEG", "JPG"]:
            raise ValueError("Format must be JPEG or JPG")

        imgArr = np.array(im)

        # --- ZOOM: crop a 400x400 region ---
        # Example: take top-left corner
        zoomed = imgArr[:400, :400]

        # Extract one channel (Red = index 0)
        zoomed_one_channel = zoomed[:, :, 0:1]

        # Print info
        print("New shape after slicing:", zoomed_one_channel.shape)
        print(zoomed_one_channel)

        plt.imshow(zoomed_one_channel.squeeze(), cmap="gray")
        plt.title("Zoomed Image (400x400)")
        plt.xlabel("X-axis (pixels)")
        plt.ylabel("Y-axis (pixels)")
        plt.show()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    ft_zoom("animal.jpeg")

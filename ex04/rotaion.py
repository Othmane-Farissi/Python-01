from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def ft_rotate(path: str):
    try:
        im = Image.open(path)

        if im.format not in ["JPEG", "JPG"]:
            raise ValueError("Format must be JPEG or JPG")

        imgArr = np.array(im)

        # --- CROP a 400x400 region from center ---
        h, w, _ = imgArr.shape
        start_x = w // 2 - 200
        start_y = h // 2 - 200
        cropped = imgArr[start_y:start_y+400, start_x:start_x+400]

        # Extract one channel (e.g., Red)
        cropped_one_channel = cropped[:, :, 0]

        print("The shape of image is:", cropped_one_channel.shape)
        print(cropped_one_channel)

        # --- TRANSPOSE manually (no numpy transpose) ---
        transposed = [[cropped_one_channel[j][i] for j in range(400)] for i in range(400)]
        transposed = np.array(transposed)

        print("New shape after Transpose:", transposed.shape)
        print(transposed)

        # --- Display both ---
        fig, axs = plt.subplots(1, 2, figsize=(8, 4))

        axs[0].imshow(cropped_one_channel, cmap="gray")
        axs[0].set_title("Original Crop")
        axs[1].imshow(transposed, cmap="gray")
        axs[1].set_title("After Transpose")

        plt.show()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    ft_rotate("animal.jpeg")

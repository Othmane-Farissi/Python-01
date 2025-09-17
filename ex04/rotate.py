import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_rotate(path: str):
    """
    Load an image, crop a 400x400 region from its center, and transpose it.

    - Uses the first channel of the image (grayscale).
    - Prints the shape and array of the cropped region.
    - Transposes the cropped image manually (swaps rows and columns).
    - Displays the original cropped image and the transposed image
      side by side.

    Args:
        path (str): The file path to the image to load.
    """
    imgArr = ft_load(path)
    h, w, _ = imgArr.shape

    start_x = w // 2 - 200
    start_y = h // 2 - 200

    cropped = imgArr[start_y:start_y+400, start_x:start_x+400]
    cropped_one_channel = cropped[:, :, 0]
    print("The shape of image is:", cropped_one_channel.shape)
    print(cropped_one_channel)

    transposed = []

    for i in range(400):
        new_row = []
        for j in range(400):
            new_row.append(cropped_one_channel[j][i])
        transposed.append(new_row)

    transposed = np.array(transposed)
    print("New shape after Transpose:", transposed.shape)
    print(transposed)

    fig, axs = plt.subplots(1, 2, figsize=(8, 4))
    axs[0].imshow(cropped_one_channel, cmap="gray")
    axs[0].set_title("Original Crop")
    axs[1].imshow(transposed, cmap="gray")
    axs[1].set_title("After Transpose")
    plt.show()


if __name__ == "__main__":
    ft_rotate("animal.jpeg")

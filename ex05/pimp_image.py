import numpy as np
import matplotlib.pyplot as plt


def ft_show(array: np.ndarray, title: str = "Image") -> None:
    """
    Displays the given image using matplotlib.
    """
    plt.imshow(array)
    plt.title(title)
    plt.axis("off")
    plt.show()


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    # 255 - pixel value
    tmp = array.copy()
    ft_show(tmp)

    return 255 - tmp


def ft_red(array) -> np.ndarray:
    """
    Keeps only the red channel of the image.
    """
    red_img = array.copy()
    red_img[:, :, 1] = red_img[:, :, 1] * 0  # zero green
    red_img[:, :, 2] = red_img[:, :, 2] * 0  # zero blue

    ft_show(red_img)
    return red_img


def ft_green(array) -> np.ndarray:
    """
    Keeps only the green channel of the image.
    """
    green_img = array.copy()
    green_img[:, :, 0] = green_img[:, :, 0] - green_img[:, :, 0]
    green_img[:, :, 2] = green_img[:, :, 2] - green_img[:, :, 2]

    ft_show(green_img)
    return green_img


def ft_blue(array) -> np.ndarray:
    """
    Keeps only the blue channel of the image.
    """
    blue_img = array.copy()
    blue_img[:, :, 0] = 0
    blue_img[:, :, 1] = 0

    ft_show(blue_img)
    return blue_img


def ft_grey(array) -> np.ndarray:
    """
    Converts the image to grayscale.
    """
    grey = (
        array[:, :, 0] / 3
        + array[:, :, 1] / 3
        + array[:, :, 2] / 3
    ).astype(np.uint8)

    grey_img = np.stack((grey, grey, grey), axis=-1)
    ft_show(grey_img)
    return grey_img

# tester.py:

# from load_image import ft_load
# from pimp_image import ft_invert
# from pimp_image import ft_red
# from pimp_image import ft_green
# from pimp_image import ft_blue
# from pimp_image import ft_grey

# array = ft_load("landscape.jpg")
# ft_invert(array)
# ft_red(array)
# ft_green(array)
# ft_blue(array)
# ft_grey(array)
# print(ft_invert.__doc__)

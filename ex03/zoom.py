from load_image import ft_load
import matplotlib.pyplot as plt


def ft_zoom(path):

    arr = ft_load(path)
    zomed = arr[:400, :400]

    zomed_one_channel = zomed[:, :, 0]

    print("New shape after slicing: ", zomed_one_channel.shape)

    plt.imshow(zomed_one_channel, cmap="gray")
    plt.title("zomed")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    ft_zoom("animal.jpeg")

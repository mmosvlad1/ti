import cv2
import numpy as np
from scipy.stats import entropy as scipy_entropy
import matplotlib.pyplot as plt


def calculate_random_entropy():
    random_sequence = np.random.randint(0, 5, np.random.randint(10, 21))
    print(random_sequence)
    random_entropy = scipy_entropy(random_sequence, base=2)
    return random_entropy


def calculate_entropy_value():
    value = [0.11, 0.10, 0.11, 0.12, 0.07, 0.08, 0.09, 0.11, 0.12, 0.10]
    entropy_value = -np.sum(value * np.log2(value + np.finfo(float).eps))
    return entropy_value


def calculate_image_entropy(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    entropy_scipy = scipy_entropy(image.flatten(), base=2)
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist = hist.astype(int)

    plt.plot(hist)
    plt.title('Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()

    return entropy_scipy


if __name__ == "__main__":
    random_entropy = calculate_random_entropy()
    entropy_value = calculate_entropy_value()
    image_entropy = calculate_image_entropy('cat3.bmp')

    print(f'Ентропія випадкової величини: {random_entropy}')
    print(f'Ентропія за виразом (2.1): {entropy_value}')
    print(f'Ентропія за допомогою SciPy: {image_entropy}')

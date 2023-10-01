import cv2
import numpy as np
from scipy.stats import entropy as scipy_entropy


def disc(img, img_path, step, *desc_levels):
    disc_images[1] = img
    for level in desc_levels:
        new_height = height // step
        new_width = width // step
        discretized_image = np.zeros((height // step, width // step), dtype=np.uint8)

        for y in range(0, new_height):
            for x in range(0, new_width):
                discretized_image[y, x] = img[y * step, x * step]

        disc_images[level] = discretized_image

    for level, discretized in disc_images.items():
        img_entropy = scipy_entropy(discretized.flatten(), base=2)
        print(f"Discretized {level} levels, entropy = {img_entropy}")
        cv2.imwrite(f'disc_{level}_{img_path}', discretized)
        cv2.imshow(f'Discretized {level} levels', discretized)
        cv2.waitKey(0)


def quant(img_path, *quant_levels):
    entropy = scipy_entropy(image.flatten(), base=2)
    for levels in quant_levels:
        for level, img in disc_images.items():
            quantized = (img // (256 // levels)) * (256 // levels)
            img_entropy = scipy_entropy(quantized.flatten(), base=2)
            print(f"Discretized {level} levels, quantized {levels} levels,"
                  f" entropy = {img_entropy}, relative entropy = {entropy - img_entropy}")

            cv2.imwrite(f'disc_{level}_quantized_{levels}_{img_path}', quantized)
            cv2.imshow(f'Disc {level} levels, quantized {levels} levels', quantized)
            cv2.waitKey(0)


def restore(img_path):
    for level, img in disc_images.items():
        if level != 1:
            nearest_restored = cv2.resize(img, (width, height), interpolation=cv2.INTER_NEAREST)
            bilinear_restored = cv2.resize(img, (width, height), interpolation=cv2.INTER_LINEAR)
            bicubic_restored = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)

            cv2.imwrite(f'nearest_restored_{level}_level_{img_path}', nearest_restored)
            cv2.imwrite(f'bilinear_restored_{level}_level{img_path}', bilinear_restored)
            cv2.imwrite(f'bicubic_restored_{level}_level{img_path}', bicubic_restored)

            cv2.imshow(f'nearest_restored {level} level', nearest_restored)
            cv2.waitKey(0)
            cv2.imshow(f'bilinear_restored {level} level', bilinear_restored)
            cv2.waitKey(0)
            cv2.imshow(f'bicubic_restored {level} level', bicubic_restored)
            cv2.waitKey(0)


if __name__ == "__main__":
    image_path = 'img.jpg'
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    height, width = image.shape
    num_gradients = len(set(image.flatten()))
    print(f"Кількість градацій на зображенні: {num_gradients}")

    disc_images = {}
    disc(image, image_path, 2, 2, 4)
    quant(image_path, 8, 16, 64)
    restore(image_path)






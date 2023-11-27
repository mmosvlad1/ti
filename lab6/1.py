import numpy as np

probabilities = np.array([[0.105, 0.025, 0.120],
                          [0.030, 0.175, 0.060],
                          [0.015, 0.050, 0.420]])


# Середня кількість інформації I(Y, X)
def information_content(probabilities):
    return -np.sum(probabilities * np.log2(probabilities))


average_information = information_content(probabilities)
print(f"Середня кількість інформації: {average_information:.4f} біт")

# Інформаційна пропускна здатність C
max_information = np.max(np.sum(probabilities, axis=0))
print(f"Інформаційна пропускна здатність: {max_information:.4f} біт")

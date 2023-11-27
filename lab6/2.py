import numpy as np

p_error = 0.02
p_erase = 0.08

p_c = 1 - p_error - p_erase


# Ентропія Бернуллі
def entropy(p):
    return -p * np.log2(p) - (1 - p) * np.log2(1 - p)


# Пропускна здатність C
capacity = np.log2(1 + p_c * (1 - entropy(p_error)) / p_error)
print(f"Пропускна здатність: {capacity:.4f} біт")

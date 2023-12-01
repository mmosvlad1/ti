import numpy as np

p_error = 0.02
p_erase = 0.08

q = 1 - p_error - p_erase

capacity_2 = q * np.log2(q) + p_error * np.log2(p_error) - (q + p_error) * np.log2((q + p_error)/2)
print(f"Пропускна здатність: {capacity_2:.4f} біт")






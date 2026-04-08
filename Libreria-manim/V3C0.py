#Aqui esta el codigo visto el 09 del 04 del 2026.

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2, 1],
              [1, 1]])

v = np.array([1, 2])
v_t = A @ v

plt.figure(figsize=(6,6))

plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.grid(True)

# Vector original (azul)
plt.quiver(0, 0, v[0], v[1],
           angles='xy',
           scale_units='xy',
           scale=1,
           color='blue',
           label='Original')

# Vector transformado (rojo)
plt.quiver(0, 0, v_t[0], v_t[1],
           angles='xy',
           scale_units='xy',
           scale=1,
           color='red',
           label='Transformado')

plt.legend()
plt.title("Transformación Lineal")
plt.show()

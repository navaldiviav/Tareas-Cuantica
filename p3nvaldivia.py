import numpy as num
import matplotlib.pyplot as plt

# Define los parámetros de la función
a = 1.0
valor_lambda = 0.3

# Definir el rango de valores de x
x = num.linspace(-10, 10, 1000)

# Definimos la función
y = num.sqrt(valor_lambda / num.pi) * num.exp(-valor_lambda * (x - a)**2)

# Gráfico de la función
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$\rho (x) \ densidad \ de \ probabilidad$', color='magenta', alpha= 0.8)
plt.title(r'$Función \ Gaussiana \ P3$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Plot del gráfico
plt.show()
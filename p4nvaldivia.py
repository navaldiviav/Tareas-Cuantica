import numpy as num
import matplotlib.pyplot as plt

# Define los parámetros de la función
a = 1.0
valor_lambda = 0.3

# Definir el rango de valores de x
x = num.linspace(-10, 10, 1000)

# Definimos la función
y = (valor_lambda) * num.exp(-2*valor_lambda * (abs(x))) # Densidad de probabilidad

xx = 1/(2*(valor_lambda)**2) # Este es <x^2> y <x> = 0 por lo tanto, <x>^2 = 0
std_dev = num.sqrt(xx)

# Gráfico de la función
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$Densidad \ de \ probabilidad$', color='magenta', alpha= 0.8)

# Gráfico de +- sigma
plt.axvline(x= std_dev, color='purple', linestyle='--', label='$+\sigma$')
plt.axvline(x= -std_dev, color='purple', linestyle=':', label='$-\sigma$')

plt.title(r'$Función \ Gaussiana \ P4$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Plot del gráfico
plt.show()
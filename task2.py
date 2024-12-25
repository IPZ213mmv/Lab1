import numpy as np
import matplotlib.pyplot as plt

# Параметри розділяючих прямих
# Прямі можна вибрати вручну, щоб вони розділяли точки XOR
def line1(x):
    return x - 0.5  # Наприклад: x1 - x2 = 0.5

def line2(x):
    return -x + 1.5  # Наприклад: -x1 + x2 = 1.5

# Точки для XOR
points = np.array([
    [0, 0, 0],  # x1, x2, XOR
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
])

# Розбиття на класи
class0 = points[points[:, 2] == 0]
class1 = points[points[:, 2] == 1]

# Графік
plt.figure(figsize=(6, 6))
plt.scatter(class0[:, 0], class0[:, 1], color='red', label='Class 0 (XOR=0)')
plt.scatter(class1[:, 0], class1[:, 1], color='blue', label='Class 1 (XOR=1)')

# Додаємо прямі
x = np.linspace(-0.5, 1.5, 100)
plt.plot(x, line1(x), label='Line 1: x1 - x2 = 0.5', color='green')
plt.plot(x, line2(x), label='Line 2: -x1 + x2 = 1.5', color='orange')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(-0.5, 1.5)
plt.ylim(-0.5, 1.5)
plt.legend()
plt.title("Двошаровий персептрон для XOR")
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Time range (in minutes)
t = np.linspace(0, 10, 200)

# First-order reaction
k1 = 0.3
C_A0 = 1.0
C_A1 = C_A0 * np.exp(-k1 * t)
X1 = 1 - C_A1 / C_A0

# Second-order reaction
k2 = 0.5
C_A2 = C_A0 / (1 + k2 * C_A0 * t)
X2 = 1 - C_A2 / C_A0

plt.figure(figsize=(10, 6))
plt.plot(t, X1, label='First-order', color='blue')
plt.plot(t, X2, label='Second-order', color='red', linestyle='--')
plt.title('Conversion vs Time for First and Second Order Reactions in a Batch Reactor')
plt.xlabel('Time (min)')
plt.ylabel('Conversion (X)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("output_plot.png")
plt.show()

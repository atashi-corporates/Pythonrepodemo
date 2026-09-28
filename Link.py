import numpy as np
import matplotlib.pyplot as plt

L1 = 10
L2 = 7

theta1 = 30
theta2 = 45

t1 = np.radians(theta1)
t2 = np.radians(theta2)

x1 = L1 * np.cos(t1)
y1 = L1 * np.sin(t1)

x2 = x1 + L2 * np.cos(t1 + t2)
y2 = y1 + L2 * np.sin(t1 + t2)

plt.plot([0, x1, x2],
         [0, y1, y2],
         marker='o')

plt.text(0, 0, "  Base")
plt.text(x1, y1, "  Joint 2")
plt.text(x2, y2, "  End Effector")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("2-Link Robot Arm - Forward Kinematics")

plt.grid()
plt.axis("equal")
plt.show()

print("Joint 2 Position:", x1, y1)
print("End-Effector Position:", x2, y2)
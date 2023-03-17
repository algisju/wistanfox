import random
import matplotlib.pyplot as plt

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_facecolor('black')
ax.set_xlim([0, 36])
ax.set_ylim([100, 150])
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')

# Generate the data for the lines
x = range(1, 37)
y1 = [random.randint(100, 120) for _ in range(36)]
y2 = [random.randint(100, 120) for _ in range(36)]
y3 = [random.randint(100, 120) for _ in range(36)]
y4 = [100 + i * 20 for i in range(36)]

# Plot the lines
ax.plot(x, y1, color='blue', linewidth=1)
ax.plot(x, y2, color='white', linewidth=1)
ax.plot(x, y3, color='green', linewidth=1)
ax.plot(x, y4, color='red', linewidth=2)

# Show the plot
plt.show()
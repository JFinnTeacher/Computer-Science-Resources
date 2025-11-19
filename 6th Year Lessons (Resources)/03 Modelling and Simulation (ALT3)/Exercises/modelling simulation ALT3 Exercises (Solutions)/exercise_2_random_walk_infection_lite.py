# Exercise 2: Random walk infection (lite)
# No classes/dicts. Optional plotting if matplotlib is installed.

import random
import math

# Parameters
N = 30
steps = 150
width, height = 80, 80
infection_radius = 2.0
infection_prob = 0.8
recovery_time = 25
social_distance = False  # True reduces step size

# State
x = [random.uniform(0, width) for _ in range(N)]
y = [random.uniform(0, height) for _ in range(N)]
infected = [False] * N
timer = [0] * N
recovered = [False] * N

# Seed
infected[0] = True
timer[0] = recovery_time

infected_counts = []

for t in range(steps):
    # Move
    for i in range(N):
        step_size = 0.6 if social_distance else 1.2
        xi = x[i] + random.uniform(-step_size, step_size)
        yi = y[i] + random.uniform(-step_size, step_size)
        x[i] = min(max(xi, 0), width)
        y[i] = min(max(yi, 0), height)

    # Spread
    for i in range(N):
        for j in range(i + 1, N):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            if math.hypot(dx, dy) <= infection_radius:
                if infected[i] and (not infected[j]) and (not recovered[j]):
                    if random.random() < infection_prob:
                        infected[j] = True
                        timer[j] = recovery_time
                elif infected[j] and (not infected[i]) and (not recovered[i]):
                    if random.random() < infection_prob:
                        infected[i] = True
                        timer[i] = recovery_time

    # Recover
    for i in range(N):
        if infected[i]:
            timer[i] -= 1
            if timer[i] <= 0:
                infected[i] = False
                recovered[i] = True

    infected_counts.append(sum(1 for v in infected if v))

print("Peak infected:", max(infected_counts))
print("Final infected:", infected_counts[-1])
print("Total recovered:", sum(1 for r in recovered if r))

# Simple text sparkline (optional)
# for c in infected_counts:
#     print("#" * c)

# Plot helpers (require matplotlib)
def plot_infected_curve(counts, title="Infected over time"):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Plot skipped: install matplotlib to enable charts (pip install matplotlib).")
        return
    plt.figure(figsize=(6, 4))
    plt.plot(range(len(counts)), counts, color="crimson")
    plt.xlabel("Step")
    plt.ylabel("Infected")
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def scatter_positions(x_list, y_list, infected_list, recovered_list, title="Agent positions"):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Plot skipped: install matplotlib to enable charts (pip install matplotlib).")
        return
    colors = []
    for inf, rec in zip(infected_list, recovered_list):
        if inf:
            colors.append("red")
        elif rec:
            colors.append("green")
        else:
            colors.append("blue")
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Plot skipped: install matplotlib to enable charts (pip install matplotlib).")
        return
    plt.figure(figsize=(5, 5))
    plt.scatter(x_list, y_list, c=colors, s=18, edgecolors="k", linewidths=0.3)
    plt.xlim(0, width)
    plt.ylim(0, height)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(title + " (blue=susceptible, red=infected, green=recovered)")
    plt.tight_layout()
    plt.show()

# Uncomment to visualize:
# plot_infected_curve(infected_counts, title="Baseline infection curve")
# scatter_positions(x, y, infected, recovered, title="Final positions")

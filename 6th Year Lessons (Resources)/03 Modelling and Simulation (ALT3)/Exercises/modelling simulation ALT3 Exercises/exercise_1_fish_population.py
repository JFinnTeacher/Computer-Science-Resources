# Exercise 1: Fish population model (deterministic)
# Edit parameters to run scenarios. Optional plotting if matplotlib is installed.

# Parameters
initial_population = 12000
years = 10
growth_rate_percent = 8  # percent per year
annual_harvest = 1500    # fixed harvest each year

population = initial_population
history = [population]

collapse_year = None

print("Year  Population")
for year in range(1, years + 1):
    growth = population * (growth_rate_percent / 100)
    population = population + growth - annual_harvest
    if population < 0:
        population = 0
    history.append(population)
    print(year, int(round(population)))
    if collapse_year is None and population < 1000:
        collapse_year = year

print("Final population:", round(population, 2))
if collapse_year is not None:
    print("Collapse threshold reached at year", collapse_year)

# Optional: percentage-based harvest scenario
# Uncomment to try:
# annual_harvest = 0.10  # 10% harvest rate
# population = initial_population
# history = [population]
# print("\n-- 10% harvest scenario --")
# for year in range(1, years + 1):
#     growth = population * (growth_rate_percent / 100)
#     harvest = population * annual_harvest
#     population = population + growth - harvest
#     if population < 0:
#         population = 0
#     history.append(population)
#     print(year, int(round(population)))
# print("Final population (10% harvest):", round(population, 2))

# Plot helper (requires matplotlib)
def plot_population(history_list, title="Fish Population over Time"):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Plot skipped: install matplotlib to enable charts (pip install matplotlib).")
        return
    years_axis = list(range(len(history_list)))
    plt.figure(figsize=(6, 4))
    plt.plot(years_axis, history_list, marker="o")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

# Uncomment to visualize:
# plot_population(history, title="Deterministic model")

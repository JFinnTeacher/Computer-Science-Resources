# Hunter prey model
# We are using the Lotka-Volterra equations - https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations,
# to model the dynamics of interacting populations of predator and prey animals, where the growth or decline in each population
# depends in part on both of the current populationsizes.

# a (alpha) = growth constant for the prey
# b (beta) = rate of predation by predator
# δ (delta) = rate at which prey is consumed
# γ (gamma) = rate of decay of predator population
# x = current prey populaiton
# y = current predator population

# Necessary plotting library matplotlib, along with the animation module to plot graph
import matplotlib.pyplot as plt

#Set your constant values
alpha = 3
beta = .1
gamma = .8
delta = .03

# These will be the lists we pass to the graphing function
# Including the xs as a list even though they're just a range to keep the plotting function looking neat
x1,y1 = [0],[50]  # Setting the starting point of the graph, co-ordinate (0,50) the x value is just a counter, y value reflects the number of prey
x2,y2 = [0],[20]  # Setting the starting point of the graph, co-ordinate (0,20) the x value is just a counter, y value reflects the number of predators

#simulate out for 100 steps
for n in range(75):
    new_y1 = y1[-1] + ((alpha - beta*y2[-1])*y1[-1])*.1  # Using the prey formula to get a new y1 value
    new_y2 = y2[-1] + ((delta*y1[-1] - gamma)*y2[-1])*.1 # Using the predator formula to get a new y2 value
    x1.append(n)      # Append loop counter to x1 list, purely to use as a co-ordinate for plotting
    y1.append(new_y1) # Append new calculated y1 value
    x2.append(n)      # Append loop counter to x2 list, purely to use as a co-ordinate for plotting
    y2.append(new_y2) # Append new calculated y2 value

# Static graph version
plt.plot(x1,y1, label='Prey') # Plotting the prey population growth
plt.plot(x2,y2, label='Predator') # Plotting the predator population growth
plt.ylabel('Population size') # Y axis label
plt.title('Rate of change of hunter/prey population growth') # Graph heading
plt.legend()                  # Legend to tell python show the labels given to each plot 
plt.show()                    # Show the plot


# Analysis
# Taken together, these two equations create periodic curves, with the prey population growing
# rapidly during periods of low predator population, only to be driven down again as
# the predator population grows

# iteration 2,3,4....
# How could you improve on this program?
# Would you change the UI or UX?
# What about a system with multiple predators or prey?
# What if there is even less/more predators/prey?
# Should the user be able to input any information?
# Do the constants change for different areas? e.g are these constants different in oceanic environments compared to African plains environments?








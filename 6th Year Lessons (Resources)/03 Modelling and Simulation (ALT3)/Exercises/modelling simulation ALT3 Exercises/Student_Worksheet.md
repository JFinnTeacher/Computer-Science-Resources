1. # Modelling & Simulation – Student Worksheet (ALT 3)

   Name:
   Class:
   Date:

   ## How to run the code (Thonny only)

   Use Thonny for all tasks.

   1) Open Thonny.
   2) File > Open… and select the .py file:
      - exercise_1_fish_population.py
      - exercise_2_random_walk_infection_lite.py
   3) Click Run ▶ or press F5 to run.
   4) To change a scenario:
      - Edit the parameter values at the top of the file (e.g., annual_harvest, social_distance).
      - Press Run ▶ again to see the new results.
   5) Optional plotting (charts):
      - Ask your teacher if matplotlib is installed.
      - If yes, uncomment the plot lines in the file (look for “Uncomment to visualize”) and Run ▶.

   Purpose
   You will explore two kinds of computer models:
   - Deterministic model (fish population): same inputs → same outputs
   - Stochastic model (random walk infection): includes randomness, so repeated runs can differ

   Learning goals (ALT 3)
   - 3.8 Develop a model to test different scenarios (by changing parameters)
   - 3.9 Analyse and interpret simulation outcomes before and after modifications
   - 3.10 Explain how agent rules can produce emergent behaviour (Exercise 2)

   How to submit
   - This worksheet (completed)
   - Your .py files with your parameter changes (add a short comment above any change)
   - Any charts you generated (optional)

   Success criteria
   - You run each model with the default parameters
   - You run at least two scenario changes per exercise
   - You record results clearly
   - You explain at least one insight per exercise (what changed and why)

   ---

   ## Exercise 1 – Fish Population (Deterministic)

   File: exercise_1_fish_population.py

   What to do
   1) Run with default parameters. Read the year-by-year output and final population.
   2) Change one parameter at a time (years, growth_rate_percent, annual_harvest) to test “what-if” scenarios.
   3) Add an early-stop rule: if population drops below 1000, print “Collapse at year X” and stop the loop.
   4) Optional: Try harvesting 10% of the population each year (see commented example in the file).
   5) Optional: If charts are available, call plot_population(history) at the end (uncomment the line).

   Record your parameters (before running)
   - Default:
     - initial_population:
     - years:
     - growth_rate_percent:
     - annual_harvest:

   Scenario A (change ONE parameter):
   - Changed parameter and value:
   - Prediction (what you expect):

   Scenario B (change ONE parameter, different from A):
   - Changed parameter and value:
   - Prediction:

   Results (fill in after running)
   - Default run: final population =      ; collapse year (if any) =
   - Scenario A: final population =       ; collapse year (if any) =
   - Scenario B: final population =       ; collapse year (if any) =

   If you plotted a chart, briefly describe the trend:
   - Curve shape (increasing/flat/declining; any equilibrium?):

   Questions
   1) Is the population sustainable under the default parameters? Give evidence (numbers or chart).

   2) Which parameter had the biggest effect in your tests (growth % vs harvest vs years)? Why?

   3) Name one unrealistic assumption. How could you improve it? (e.g., carrying capacity K, harvest quota)

   Checklist
   - I changed exactly one parameter per scenario
   - I recorded before/after results and any collapse
   - I wrote at least one clear insight

   ---

   ## Exercise 2 – Random Walk Infection (Stochastic)

   File: exercise_2_random_walk_infection_lite.py

   What to know
   - Because of randomness, identical settings can give different results each time.
   - Key outputs: Peak infected, Final infected, Total recovered.
   - Optional charts:
     - plot_infected_curve(infected_counts)
     - scatter_positions(x, y, infected, recovered)

   What to do
   1) Baseline:
      - Run the program 3 times without changing parameters.
      - Record the peak infected each time and compare.
   2) Scenario A (social distancing):
      - Set social_distance = True and run once.
      - Record peak infected and total recovered.
   3) Scenario B (contact radius):
      - Set infection_radius = 1.0 and run once.
      - Record peak infected and total recovered.
   4) Sensitivity:
      - Set infection_prob = 0.4 (run once) and then 0.95 (run once).
      - Compare how quickly and how widely infection spreads.

   Baseline results (3 runs)
   - Run 1: peak infected =
   - Run 2: peak infected =
   - Run 3: peak infected =
   Average peak =

   Scenario results
   - Scenario A (social_distance = True)
     - Peak infected =
     - Total recovered =
   - Scenario B (infection_radius = 1.0)
     - Peak infected =
     - Total recovered =
   - Sensitivity (infection_prob = 0.4)
     - Peak infected =
     - Total recovered =
   - Sensitivity (infection_prob = 0.95)
     - Peak infected =
     - Total recovered =

   If you plotted a chart, briefly describe observations:
   - Infection curve shape (speed to peak, height of peak, tail):
   - Final positions scatter (more clustering or more spread?):

   Questions
   1) Why did the three baseline runs produce different peaks even with the same settings?

   2) Which change most reduced peak infections: social distancing, smaller infection radius, or lower infection probability? Explain.

   3) Give one example of emergent behaviour you observed (e.g., clusters triggering outbreaks, quick burn-out).

   Checklist
   - I ran 3 baseline trials and recorded peaks
   - I ran both scenarios and at least one sensitivity test
   - I explained at least one emergent pattern

   ---

   ## Reflection across both exercises

   Short paragraph (5–7 sentences)
   - Compare deterministic vs stochastic models: how do their outputs and your testing approach differ?
   - One benefit of modelling and one limitation you noticed.
   - One change you would make to improve realism in either model, and why.

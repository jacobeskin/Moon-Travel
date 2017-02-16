import itertools
import numpy as np
import matplotlib.pyplot as plot

# Calculate the travel time to moon with Newtons law of 
# gravity and second law of motion where derivatives are
# evaluated with simple Eulers method. This script shows 
# how the choice in the magnitude of the time step affects
# the total calculated travel time by plotting time step vs.
# travel time. This script was originally written in Finnish,
# variable names reflect that.

# Define constants and initialize the time step vector
g = 6.674*(10**(-11))  # Gravitational constant
Maa = 5.974*(10**24)   # Earths mass
Kuu = 7.348*(10**22)   # Moons mass
X = 376000000          # Target distance, low orbit of moon (Wikipedia)
T = np.zeros(100)      # Vector for housing travel times
DT = np.arange(101)    # Vector for housing time steps
DT = DT[1:]

# Calcualte travel time with different time step sizes
for dt in range(1,101):
    n = 0                 # Keeps track of # time steps
    r1 = 6578100          # Distance from Earths center in the beginning
    v1 = 12012            # Initial velocity + 10%
    for i in itertools.count():
         n = n+1
         # New distance
         r = r1+v1*dt                     
         # Update acceleration term
         b = Kuu/((3844*(10**5)-r1)**2) 
         c = Maa/(r1**2)
         A = g*(b-c)
         # New velocity
         v = v1+A*dt
         # Update position and velocity
         r1 = r
         v1 = v
         # If we have arrived to the moon!
         if r>=X:
            T[dt-1] = (n*dt)/3600
            break
         

# Plot results

plot.plot(DT,T)
plot.xlabel('Aika-askel, s') # "Aika-askel" means time step
plot.ylabel('Matka-aika, h') # "Matka-aika" means travel time
plot.show()
    
    




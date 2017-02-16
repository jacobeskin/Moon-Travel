import itertools
import numpy as np
import matplotlib.pyplot as plot

# Numerical calculation and visualisation of the change in position
# and velocity of a spacecraft when it travels to the moon. Newtons 
# law of gravitation and second law of motion are used. Derivative is
# evaluated with simple Euler method. This project was originally
# done in Finnish, the variable names reflect that.

# Define constants and vectors for position and velocity
g = 6.674*(10**(-11))  # Gravitation constant
Maa = 5.974*(10**24)   # Earths mass
Kuu = 7.348*(10**22)   # Moons mass
X = 376084800          # Target distance, low orbit of moon (Wikipedia)
n = 0                  # Keeps tab on how many time steps has gone
r1 = 6578100           # Distance from Earths center in the beginning
v1 = 12012             # Starting velocity + 10%
V = np.array([v1])     # Vector that will house the values of velocity
R = np.array([r1])     # Vector that will house the values of distance

dt = 10                 # Length of time step in seconds

# Iterate our way to the moon!
for i in itertools.count():
    n = n+1
    # New distance
    r = r1+v1*dt   
    R = np.append(R,r)
    # Updated acceleration
    b = Kuu/((3844*(10**5)-r1)**2) 
    c = Maa/(r1**2)
    A = g*(b-c)
    # New velocity
    v = v1+A*dt
    V = np.append(V,v)
    # Update position and velocity
    r1 = r
    v1 = v
    # When arriving to the moon
    if r>=X:
        break

T = (n*dt)/3600        # Travel time in hours

print(T)

# Plot the graphs of position and velocity as function of time

plot.figure(1)
plot.subplot(211)
plot.plot(R)
plot.xlabel('Aika, s')      # "Aika" means time
plot.ylabel('Matka, m')     # "Matka" means distance

plot.subplot(212)
plot.plot(V)
plot.xlabel('Aika, s')
plot.ylabel('Nopeus, m/s')  # "Nopeus" means velocity

plot.show()

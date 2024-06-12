#Assignment 2
N_left = 1  # Number of cashiers in the left 
R_left = 4  # Number of users in the left 
T = 24  # Time in hours

N_right = 4  # Number of cashiers in the right 
R_right = 4  # Number of users in the right 

# Calculation power consumption for both scenarios
P_left = N_left * R_left * T
P_right = N_right * R_right * T


print(f"Power consumption for the left scenario (self-checkout lanes): {P_left} watt-hours")
print(f"Power consumption for the right scenario (individual checkout lanes): {P_right} watt-hours")

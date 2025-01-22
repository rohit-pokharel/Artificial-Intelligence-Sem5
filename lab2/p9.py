import random
import math
import matplotlib.pyplot as plt

# Example Objective Function: Minimizing the quadratic function f(x) = x^2
def objective_function(x):
    return x ** 2

# Generate a random neighbor by slightly modifying the current solution
def generate_neighbor(x):
    return x + random.uniform(-1, 1)

# Simulated Annealing with temperature schedule
def simulated_annealing(initial_temp, cooling_rate, iterations):
    current_solution = random.uniform(-10, 10)  # Start with a random solution
    current_value = objective_function(current_solution)
    
    temperature = initial_temp
    values = []  # To store the objective values for plotting
    
    for k in range(iterations):
        neighbor = generate_neighbor(current_solution)
        neighbor_value = objective_function(neighbor)
        
        # Calculate the change in objective function
        delta_e = neighbor_value - current_value
        
        # If the neighbor is better, always accept it
        if delta_e < 0:
            current_solution = neighbor
            current_value = neighbor_value
        # If the neighbor is worse, accept it with a probability
        else:
            probability = math.exp(-delta_e / temperature)
            if random.random() < probability:
                current_solution = neighbor
                current_value = neighbor_value
        
        # Decrease the temperature
        temperature *= cooling_rate
        
        # Store the value for plotting
        values.append(current_value)
    
    return current_solution, current_value, values

# Parameters
initial_temp = 10  # Initial temperature
cooling_rate = 0.99  # Cooling rate
iterations = 500  # Number of iterations

# Run Simulated Annealing
final_solution, final_value, values = simulated_annealing(initial_temp, cooling_rate, iterations)

# Plot the change in objective value over iterations to show the effect of temperature
plt.plot(values)
plt.xlabel('Iterations')
plt.ylabel('Objective Function Value (f(x) = x^2)')
plt.title('Effect of Temperature on Accepting Inferior Nodes (Simulated Annealing)')
plt.show()

# Print final solution and value
print(f"Final solution: {final_solution}")
print(f"Final value of objective function: {final_value}")


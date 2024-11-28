import numpy as np

# Define the number of unique items in the set
n = 10

# Define the number of simulations to run
simulations = 100

# Initialize an empty list to store the number of samples for each simulation
samples_list = []

# Loop over the number of simulations
for i in range(simulations):
    # Initialize an empty set to store the unique items collected
    unique_items = set()
    # Initialize a counter for the number of samples
    samples = 0
    # Loop until every unique item is collected
    while len(unique_items) < n:
        # Generate a random sample with replacement from the set 1, ..., n
        sample = np.random.choice(n) + 1
        # Increment the number of samples
        samples += 1
        # Add the sample to the set of unique items
        unique_items.add(sample)
    # Append the number of samples to the list
    samples_list.append(samples)

# Compute the average number of samples from the simulations
sim_mean = np.mean(samples_list)

# Compute the theoretical value from the formula
theo_mean = n * np.sum(1 / np.arange(1, n + 1))

# Print the results
print(f"Average number of samples from {simulations} simulations: {sim_mean}")
print(f"Theoretical value from the formula: {theo_mean}")

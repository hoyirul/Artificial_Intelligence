import numpy
import ga
# Inputs of the equation.
equation_inputs = [4,-2,3.5,5,-11,-4.7]
# Number of the weights we are looking to optimize.
num_weights = 6

sol_per_pop = 8 # Defining the population size.
pop_size = (sol_per_pop,num_weights) # The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
#Creating the initial population.
new_population = numpy.random.uniform(low=-4.0, high=4.0, size=pop_size)

# import ga
num_generations = 5
num_parents_mating = 4
for generation in range(num_generations):
    # Measuring the fitness of each chromosome in the population.
    fitness = ga.cal_pop_fitness(equation_inputs, new_population)
    # Selecting the best parents in the population for mating.
    parents = ga.select_mating_pool(new_population, fitness,
    num_parents_mating)
    # Generating next generation using crossover.
    offspring_crossover = ga.crossover(parents,
    offspring_size=(pop_size[0]-parents.shape[0], num_weights))
    # Adding some variations to the offsrping using mutation.
    offspring_mutation = ga.mutation(offspring_crossover)# Creating the new population based on the parents and offspring.
    new_population[0:parents.shape[0], :] = parents
import string
import numpy as np
from qrl_graph.utils import np2str

class GeneticAlgorithm():
    """An implementation of a Genetic Algorithm which will try to produce the user
    specified target string.

    Parameters:
    -----------
    dimensiom: int
        The dimension for the approximate integer programming problems. 
    population_size: int
        The number of individuals (possible solutions) in the population.
    mutation_rate: float
        The rate (or probability) of which the alleles (chars in this case) should be
        randomly changed.
    """
    def __init__(self, dimension, population_size, mutation_rate, score_fn, variable_type='bool'):
        self.dimension = dimension
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.score_fn = score_fn
        if variable_type == 'bool':
            self.var_space = 2 # todo: whether to use the name (action_space)?

    def _initialize(self):
        """ Initialize population with random bit-strings """
        self.population = []
        for _ in range(self.population_size):
            # Select random letters as new individual
            individual = "".join(np2str(np.random.randint(self.var_space, size=(self.dimension,))))
            self.population.append(individual)

    def _calculate_fitness(self):
        """ Calculates the fitness of each individual in the population """
        population_fitness = []
        for individual in self.population:
            # Calculate fitness of each individual
            fitness = self.score_fn(individual)
            population_fitness.append(fitness)
        return population_fitness

    def _mutate(self, individual):
        """ Randomly change the individual's characters with probability
        self.mutation_rate """
        individual = list(individual)
        for j in range(len(individual)):
            # Make change with probability mutation_rate
            if np.random.random() < self.mutation_rate:
                individual[j] = str(np.random.randint(self.var_space))
        # Return mutated individual as string
        return "".join(individual)

    def _crossover(self, parent1, parent2):
        """ Create children from parents by crossover """
        # Select random crossover point
        cross_i = np.random.randint(0, len(parent1))
        child1 = parent1[:cross_i] + parent2[cross_i:]
        child2 = parent2[:cross_i] + parent1[cross_i:]
        return child1, child2

    def run(self, iterations):
        # Initialize new population
        self._initialize()

        history_best = 0
        history_best_individual = None
        for epoch in range(iterations):
            population_fitness = self._calculate_fitness()

            fittest_individual = self.population[np.argmax(population_fitness)]
            highest_fitness = max(population_fitness)
            if history_best_individual is None or highest_fitness > history_best:
                history_best_individual = fittest_individual
            history_best = max(history_best, highest_fitness)

            # If we have found individual which matches the target => Done
            # if fittest_individual == self.target:
                # break
            if highest_fitness == 1e6:
                break

            # Set the probability that the individual should be selected as a parent
            # proportionate to the individual's fitness.
            parent_probabilities = [fitness / sum(population_fitness) for fitness in population_fitness]

            # Determine the next generation
            new_population = []
            for i in np.arange(0, self.population_size, 2):
                # Select two parents randomly according to probabilities
                parent1, parent2 = np.random.choice(self.population, size=2, p=parent_probabilities, replace=False)
                # Perform crossover to produce offspring
                child1, child2 = self._crossover(parent1, parent2)
                # Save mutated offspring for next generation
                new_population += [self._mutate(child1), self._mutate(child2)]
            print ("[%d Closest Candidate: '%s', Fitness: %.2f] (hist record: %.2f, hist Candidate: '%s')" % (epoch, fittest_individual, highest_fitness, history_best, history_best_individual))
            self.population = new_population

        print ("[%d Answer: '%s']" % (epoch, fittest_individual))

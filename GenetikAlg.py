import random

# Konfigürasyon değişkenleri global alana çekildi
TARGET_WORD = "AHMETGOK"
CHROMOSOME_LENGTH = len(TARGET_WORD)
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','Y','Z']
MUTATION_RATE = 0.05

def generate_chromosome(length):
    chromosome = []
    for _ in range(length):
        selected = random.choice(ALPHABET)
        chromosome.append(selected)
    return chromosome

def generate_population(population_size, length):
    population = []
    for _ in range(population_size):
        individual = generate_chromosome(length)
        population.append(individual)
    return population

def calculate_fitness(individual, target):
    fitness_score = 0
    for j in range(len(target)):
        if individual[j] == target[j]:
            fitness_score += 1
    return fitness_score            

def selection(current_population, target):
    fitness_scores = []
    for individual in current_population:
        ind_fitness = calculate_fitness(individual, target)
        fitness_scores.append(ind_fitness)
        
    scored_population = []
    for i in range(len(current_population)):
        combined = [fitness_scores[i], current_population[i]]
        scored_population.append(combined)

    scored_population.sort(reverse=True)

    mating_pool_size = len(scored_population) // 2
    
    best_score = scored_population[0][0]
    best_individual = scored_population[0][1]
    
    mating_pool = scored_population[:mating_pool_size]
    
    print("En yüksek fitness değerine sahip bireyler: ", mating_pool)
    
    return mating_pool, best_score, best_individual

def crossover(mating_pool, target_population_size, length):
    next_generation = []
    parent_count = len(mating_pool)
    offspring_count = target_population_size - parent_count
    
    for _ in range(offspring_count):
        parents = random.sample(mating_pool, 2)
        parent1 = parents[0][1]
        parent2 = parents[1][1]

        # Çaprazlama noktası kelime uzunluğuna göre dinamik hale getirildi
        crossover_point = random.randint(1, length - 1)

        child = parent1[:crossover_point] + parent2[crossover_point:]
        next_generation.append(child)
        
    for j in mating_pool:
        chromosome = j[1]
        next_generation.append(chromosome)
        
    print("-" * 20)
    print("Oluşan yeni nesil: ", next_generation)
    
    return next_generation, offspring_count
        
def mutation(population, offspring_count, length):
    for i in range(offspring_count):
        for j in range(length):
            if random.random() < MUTATION_RATE:
                old_gene = population[i][j]
                new_gene = random.choice(ALPHABET)
                population[i][j] = new_gene
                
                print(f"Mutasyon:{i+1}. Çocuğun,{j+1}. Geni değişti.({old_gene}->{new_gene})")
                
    return population            

if __name__ == "__main__":
    population_size = int(input('Popülasyon Kaç Bireyden Oluşsun?: '))
    population = generate_population(population_size, CHROMOSOME_LENGTH)
    generation = 1

    while True:
        mating_pool, best_score, best_chromosome = selection(population, TARGET_WORD)
        
        print(f"\nJenerasyon: {generation} | En İyi Puan: {best_score} | En İyi Birey: {best_chromosome}")

        # Bitiş koşulu artık dinamik kelime uzunluğuna bağlı
        if best_score == CHROMOSOME_LENGTH:
            print(f"Hedef Kelime: {''.join(best_chromosome)}")
            print(f"Toplam Jenerasyon: {generation}")
            break
        
        next_generation, offspring_count = crossover(mating_pool, population_size, CHROMOSOME_LENGTH)
        mutated_generation = mutation(next_generation, offspring_count, CHROMOSOME_LENGTH)
        population = mutated_generation
        generation += 1

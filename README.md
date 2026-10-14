# Genetic Algorithm Implementation 🧬

This repository contains a Python implementation of a **Genetic Algorithm (GA)**, designed to solve optimization problems by simulating the process of natural selection.

##  About The Project
This project demonstrates the core concepts of Evolutionary Algorithms. It initializes a population of candidate solutions and evolves them over generations to find the optimal solution based on a specific fitness function.

### Key Features
* **Population Initialization:** Generates random candidate solutions.
* **Fitness Function:** Evaluates how well a candidate solves the problem.
* **Selection:** Selects the best genes (parents) for the next generation.
* **Crossover:** Combines parents to create new offspring.
* **Mutation:** Introduces random changes to maintain diversity and prevent premature convergence.

##  Built With
* **Python 3.x**
* 
## 💻 How to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/goktugkarakokcek/Genetic-Algorithm.git

   cd Genetic-Algorithm

   python GeneticAlg.py

## ⚠️ Project Scope and Limitations (Toy Problem)

This project is a foundational "Toy Problem" developed strictly for educational purposes to understand the core mechanics of Genetic Algorithms (GAs). 

**Key Technical Notes:**
* **Architecture:** Uses a basic string-matching fitness function and Truncation Selection.
* **Limitations:** The extreme elitism (retaining 50% of the population) and single-point crossover mechanics make it prone to premature convergence. 
* **Disclaimer:** This specific architecture is **not** suitable for real-world, complex optimization tasks (such as the Traveling Salesperson Problem or routing algorithms), which require permutation-based chromosomes (e.g., Order Crossover) and proportional selection methods (e.g., Tournament or Roulette Wheel Selection). 

This repository serves as a baseline learning experiment before moving on to advanced, constraint-based optimization models.

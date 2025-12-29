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

##  How to Run
1. Clone the repository:
   ```sh
   git clone [https://github.com/goktugkarakokcek/Genetic-Algorithm.git](https://github.com/goktugkarakokcek/Genetic-Algorithm.git)
   cd Genetic-Algorithm
   python GenetikAlg.py
## Example Output
Mutasyon: 3. Çocuğun, 1. Geni değişti.(Z->A)
En yüksek fitness değerine sahip bireyler: [[8, ['A', 'H', 'M', 'E', 'T', 'G', 'O', 'K']], ...]

Jenerasyon: 334 | En İyi Puan: 8 | En İyi Birey: ['A', 'H', 'M', 'E', 'T', 'G', 'O', 'K']
Hedef Kelime: ['A', 'H', 'M', 'E', 'T', 'G', 'O', 'K']
Toplam Jenerasyon: 334

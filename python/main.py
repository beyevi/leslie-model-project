"""
Main module
"""


import pandas as pd
import numpy as np

import data_reader
import build_leslie
import matrix_to_power


def get_population_vector(path_to_data: str) -> pd.DataFrame:
    """
    Get a population vector, which will be the starting point for the Leslie model
    """
    n0 = np.zeros((100, 1))
    mean_population = []

    data = (pd.read_csv(path_to_data))[['Location', 'Time', 'AgeGrp', 'PopFemale']]
    data = data[data['Location'] == 'Ukraine']
    data = data[data['Time'].isin(range(1950, 2001))]


    for i in range(100):
        selected_data = data[data['AgeGrp'] == i]
        selected_data['PopFemale'] *= 1000
        mean_population.append(sum(selected_data['PopFemale']) / 50)

    for j in range(100):
        n0[j, 0] = mean_population[j]

    return n0


if __name__ == "__main__":
    print("Building a population vector".center(100, "="))
    n_0 = get_population_vector("./data/population_single_age_sex_2019.csv")
    print(n_0)
    
    print("Building a Leslie matrix".center(100, "="))
    fertility_data = data_reader.get_fertility_data("./data/fertility.csv")
    mortality_data = data_reader.get_mortality_data("./data/mortality.csv")
    population_data = data_reader.get_population_data("./data/population_single_age_sex_2019.csv")
    
    leslie_matrix = build_leslie.build_leslie(100, fertility_data, mortality_data, population_data)
    np.savetxt("Leslie matrix.txt", leslie_matrix)
    print("The Leslie matrix has been written to 'Leslie matrix.txt'".center(100, ' '))

    print("Predicting population using Leslie matrix (immediate next gen.)".center(100, "="))
    n_1 = np.dot(leslie_matrix, n_0)
    print(n_1)

    print("Predicting population using Leslie matrix (k next gen-s.)".center(100, "="))
    for k in range(10):
        leslie_k = matrix_to_power.to_power_diag(leslie_matrix, k+1)
        n_k = np.dot(leslie_k, n_0)
        print(f"n_k, k={k}:")
        print(n_k, "\n")

"""
Python module to build a Leslie matrix
"""


import numpy as np
import data_reader


def multiply_matrices(matrix1, matrix2):
    """
    General matrix multiplication algorithm
    """
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Matrices must have same number of columns")

    result = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            cell = 0
            for k in range(cols1):
                cell += matrix1[i][k] * matrix2[k][j]
            row.append(cell)
        result.append(row)

    return result


def get_survival_rate_for_age_group(age_grp, pop, mort):
    """
    For each age class calculate the probability of entering the next age class
    
    :param pop: population dataframe
    :param mort: mortality dataframe
    """
    births, deaths, survival_rates = [], [], []

    pop_age_grp = pop[pop['AgeGrp'] == age_grp]
    mort_age_grp = mort[mort['AgeGrp'] == str(age_grp)]

    for _, row in pop_age_grp.iterrows():
        births.append(row['PopFemale'])
    for _, new_row in mort_age_grp.iterrows():
        deaths.append(new_row['DeathFemale'])

    for entry in zip(births, deaths):
        survival_rate: float = 1 - (entry[1] / entry[0])
        survival_rates.append(survival_rate)

    return sum(survival_rates) / len(survival_rates)


def get_fertility_for_age_group(age_grp, fert):
    """
    For each age class calculate the probability of entering the next age class
    
    :param age_grp: desired age class
    :param fert: fertility dataframe
    """
    if not 15 <= age_grp <= 49:
        return 0

    selected_fertility_data = fert[fert['AgeGrp'] == age_grp]

    asfr = []
    for _, row in selected_fertility_data.iterrows():
        asfr.append(row['ASFR'])

    return sum(asfr) / len(asfr)


def build_leslie(size, fert, mort, pop):
    """
    Build a Leslie matrix for a goven number of age classes
    based on fertilities and survival rates
    
    :param size: matrix size & number of age classes
    :param fert: fertility dataframe
    :param mort: mortality dataframe
    :param pop: population dataframe
    """
    fertilities = np.zeros(size)
    for i in range(size):
        fert_for_age_grp = get_fertility_for_age_group(i, fert)
        fertilities[i] = fert_for_age_grp

    mortalities = np.zeros((size - 1, size))
    counter = 0

    for s in range(size - 1):
        survival_rate = get_survival_rate_for_age_group(counter, pop, mort)
        mortalities[s][counter] = survival_rate
        counter += 1

    leslie = np.vstack([fertilities, mortalities])

    return leslie


if __name__ == "__main__":
    # On Linux device
    # fertility_data = data_reader.get_fertility_data("./data/fertility.csv")
    # mortaliti_data = data_reader.get_mortality_data("./data/mortality.csv")
    # population_data = data_reader.get_population_data("./data/population_single_age_sex_2019.csv")

    # On Windows device
    fertility_data = data_reader.get_fertility_data("../main_data/fertility.csv")
    mortaliti_data = data_reader.get_mortality_data("../main_data/mortality.csv")
    population_data = data_reader.get_population_data("../data/population_single_age_sex_2019.csv")

    leslie_matrix = build_leslie(100, fertility_data, mortaliti_data, population_data)

    np.savetxt("leslie.txt", leslie_matrix)

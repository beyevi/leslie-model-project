"""
Read CSV files using pandas
"""


import pandas as pd


def get_fertility_data(path_to_fertility):
    """
    Read CSV file with fertilities for females and return a cleaned
    dataframe with only required data
    
    :param path_to_fertility: path to CSV file with fertilities
    """
    fert = pd.read_csv(path_to_fertility)
    cleaned_fert = fert[['Location', 'Time', 'AgeGrp', 'ASFR', 'Births']]
    cleaned_fert = cleaned_fert[cleaned_fert['Location'] == 'Ukraine']
    ukraine_fert = cleaned_fert[cleaned_fert['Time'].isin(range(1950, 2001))]

    return ukraine_fert


def get_mortality_data(path_to_mortality):
    """
    Read CSV file with mortalities and return a cleaned
    dataframe with only required data
    
    :param path_to_mortality: path to CSV file with mortalities
    """
    mort = pd.read_csv(path_to_mortality)
    cleaned_mort = mort[['Location', 'Time', 'AgeGrp', 'DeathFemale']]
    cleaned_mort = cleaned_mort[cleaned_mort['Location'] == 'Ukraine']
    ukraine_mort = cleaned_mort[cleaned_mort['Time'].isin(range(1950, 2001))]

    return ukraine_mort


def get_population_data(path_to_population):
    """
    Read CSV file with population and return a cleaned
    dataframe with only required data
    
    :param path_to_population: path to CSV file with population
    """
    pop = pd.read_csv(path_to_population)
    cleaned_population = pop[['Location', 'Time', 'AgeGrp', 'PopFemale']]
    cleaned_population = cleaned_population[cleaned_population['Location'] == 'Ukraine']
    ukrainian_population = cleaned_population[cleaned_population['Time'].isin(range(1950, 2001))]
    return ukrainian_population


if __name__ == '__main__':
    fertility = get_fertility_data('../main_data/fertility.csv')
    mortality = get_mortality_data('../main_data/mortality.csv')
    population = get_population_data('../data/population_single_age_sex_2019.csv')

    print(f"{population=}")
    print(f"{mortality=}")
    print(f"{fertility=}")

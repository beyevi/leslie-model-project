import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def matrix_multiply(A, B):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]


def solve_equations(A, B):
    n = len(A)
    for i in range(n):
        max_row = max(range(i, n), key=lambda x: abs(A[x][i]))
        A[i], A[max_row] = A[max_row], A[i]
        B[i], B[max_row] = B[max_row], B[i]

        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            B[j][0] -= factor * B[i][0]

    X = [[0.0] for _ in range(n)]
    for i in range(n - 1, -1, -1):
        X[i][0] = B[i][0] / A[i][i]
        for j in range(i - 1, -1, -1):
            B[j][0] -= A[j][i] * X[i][0]

    return X


def least_squares(X, Y):
    XT = transpose(X)
    XTX = matrix_multiply(XT, X)
    XTY = matrix_multiply(XT, Y)
    coefs = solve_equations(XTX, XTY)
    return coefs


def polynomial_regression(x, beta):
    return beta[0][0]*x**2 + beta[1][0]*x + beta[2][0]


if __name__ == "__main__":
    data = pd.read_csv('WPP2022_POP_F02_1_POPULATION_5-YEAR_AGE_GROUPS_BOTH_SEXES.csv', delimiter=';')
    data = data.loc[data['Region, subregion, country or area *'] == 'Ukraine']
    columns_to_drop = ['Variant', 'Index', 'Location code', 'Notes', 'ISO3 Alpha-code', 'ISO2 Alpha-code','SDMX code**', 'Type', 'Parent code']
    data = data.drop(columns=columns_to_drop)

    data2 = pd.read_csv('WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT_REV1.csv', delimiter=';')
    data2 = data2.loc[data2['Region, subregion, country or area *'] == 'Ukraine']
    columns_to_drop = ['Variant', 'Index', 'Location code', 'Notes', 'ISO3 Alpha-code', 'ISO2 Alpha-code','SDMX code**', 'Type', 'Parent code', 'Median Age, as of 1 July (years)']
    data2 = data2.drop(columns=columns_to_drop)

    years = data2.loc[data2["Year"] <= 2000]["Year"].to_list()
    years = [[x**2, x, 1] for x in years]
    population = data2.loc[data2["Year"] <= 2000]["Total Population, as of 1 July (thousands)"].to_list()
    population = [[int(i.replace(' ', ''))] for i in population]

    beta = least_squares(years, population)
    print("Coefficients (beta):", beta)
    
    x_values = np.linspace(min([x[1] for x in years]), max([x[1] for x in years]), 100)

    y_values = [polynomial_regression(x, beta) for x in x_values]

    plt.figure(figsize=(10, 6))
    # years = data2.loc[data2["Year"] <= 2000]["Year"].to_list()
    # years = [[x,1] for x in years]
    # population = data2.loc[data2["Year"] <= 2000]["Total Population, as of 1 July (thousands)"].to_list()
    # lalala= data2.loc[data2["Year"]].to_list()
    # lalala = [[x,1] for x in lalala]

    # hui = data2.loc[data2["Total Population, as of 1 July (thousands)"]].to_list()
    plt.plot([x[1] for x in years], [y[0] for y in population], 'bo', label='Original Data')
    plt.plot(x_values, y_values, 'r-', label='Polynomial Regression (Degree 2)')
    plt.title('Polynomial Regression: Population vs Year')
    plt.xlabel('Year')
    plt.ylabel('Population (thousands)')
    plt.legend()
    plt.grid(True)
    plt.show()

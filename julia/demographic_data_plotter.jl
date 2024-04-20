using CSV
using DataFrames
using Plots


"""
Display population of Ukraine over time from 1950 until 2000
"""
function plot_population()
    population = CSV.read("./main_data/population.csv", DataFrame)

    desired_data = [:Location, :Time, :PopTotal]

    selected_data = select(population, desired_data)

    grouped_data = combine(groupby(selected_data, [:Location, :Time])) do df
        DataFrame(PopTotal = sum(df[:, :PopTotal]))
    end

    rename!(grouped_data, :Location => :Country, :Time => :Year)

    ukraine_population_data = filter(row -> row.Country == "Ukraine", grouped_data)
    ukraine_population_data = filter(row -> row.Year <= 2000, ukraine_population_data)

    show(ukraine_population_data)

    years = ukraine_population_data.Year
    pop_total = ukraine_population_data.PopTotal

    display(plot(
        years,
        pop_total,
        xlabel="Year",
        ylabel="Population",
        title="Population of Ukraine Over Time",
        legend=false,
    ))
end


"""
Display mortality in Ukraine over time from 1950 until 2000
"""
function plot_mortality()
    mortality = CSV.read("./main_data/mortality.csv", DataFrame)

    desired_data = [:Location, :Time, :AgeGrp, :DeathTotal]

    selected_data = select(mortality, desired_data)

    grouped_data = combine(groupby(selected_data, [:Location, :Time])) do df
        DataFrame(DeathTotal = sum(df[:, :DeathTotal]))
    end

    rename!(grouped_data, :Location => :Country, :Time => :Year)

    ukraine_mortality_data = filter(row -> row.Country == "Ukraine", grouped_data)
    ukraine_mortality_data = filter(row -> row.Year <= 2000, ukraine_mortality_data)

    show(ukraine_mortality_data)

    years = ukraine_mortality_data.Year
    mortality_total = ukraine_mortality_data.DeathTotal

    display(plot(
        years,
        mortality_total,
        xlabel="Year",
        ylabel="Mortality",
        title="Mortality in Ukraine Over Time",
        legend=false,
    ))
end


"""
Display fertility in Ukraine over time from 1950 until 2000
"""
function plot_fertility()
    fertility = CSV.read("./main_data/fertility.csv", DataFrame)

    desired_data = [:Location, :Time, :AgeGrp, :ASFR]

    selected_data = select(fertility, desired_data)

    grouped_data = combine(groupby(selected_data, [:Location, :Time])) do df
        DataFrame(ASFR = sum(df[:, :ASFR]))
    end

    rename!(grouped_data, :Location => :Country, :Time => :Year)

    ukraine_fertility_data = filter(row -> row.Country == "Ukraine", grouped_data)
    ukraine_fertility_data = filter(row -> row.Year <= 2000, ukraine_fertility_data)

    show(ukraine_fertility_data)

    years = ukraine_fertility_data.Year
    fertility_total = ukraine_fertility_data.ASFR

    display(plot(
        years,
        fertility_total,
        xlabel="Year",
        ylabel="Fertility Rate per 1000",
        title="Fertility in Ukraine Over Time",
        legend=false,
    ))
end


if Main == @__MODULE__
    pop_header = repeat("=", 15) * " Ukraine Population " * repeat("=", 15)
    mort_header = repeat("=", 15) * " Ukraine Mortality " * repeat("=", 15)
    fert_header = repeat("=", 15) * " Ukraine Fertility " * repeat("=", 15)


    println(pop_header)
    plot_population()
    println()

    println(mort_header)
    plot_mortality()
    println()

    println(fert_header)
    plot_fertility()
    println()

end
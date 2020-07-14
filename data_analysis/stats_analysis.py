import pandas as pd
import matplotlib.pyplot as plt
import datetime
import seaborn as sns

population_data = pd.read_excel ('Country projection by population group, sex and age (2002-2020).xlsx', sheet_name = 'Sheet1')

#select rows and columns that represent population growth
population_growth = population_data.iloc[[3, 140], 3:22]

#set columns in the first row as headings
population_growth.columns = [2002, 2003, 2004, 2005, 2006, 2007,
                             2008, 2009, 2010, 2011, 2012, 2013,
                             2014, 2015, 2016, 2017, 2018, 2019, 2020]

population_growth = population_growth.iloc[1, 0:22]

#convert population values into int
for x in range(19):
    population_growth.iloc[x] = population_growth.iloc[x]/1000000

SA = population_growth.T.plot.bar(color = '#40cfcc', title = 'South Africa population trends (2002 to 2020)')
SA.set_xlabel("Year")
SA.set_ylabel("Population (Million)")


population_by_sex_and_age = population_data.iloc[4:38, [23, 24, 43]]
population_by_sex_and_age.columns = ['Sex', 'Age', 'Population \n(Thousand)']
male_population_by_age = population_by_sex_and_age.iloc[0:17, [1, 2]]
female_population_by_age = population_by_sex_and_age.iloc[17:35, [1, 2]]

for x in range(17):
    female_population_by_age.iloc[x, 1] = female_population_by_age.iloc[x, 1]/1E6
    male_population_by_age.iloc[x, 1] = male_population_by_age.iloc[x, 1]/1E6

fig, (ax, ax2) = plt.subplots(ncols=2, sharey=True)
ax.yaxis.tick_right()
ax.set_xlim(0,3)
ax.invert_xaxis()
fig.subplots_adjust(wspace=0.25)

female_population_by_age.plot.barh(ax = ax, color = '#40cfcc', title = 'Age distribution of\n South Africa female \n population')
male_population_by_age.plot.barh(x = 'Age', ax = ax2, color = '#40cfcc',title = 'Age distribution of\n South Africa male \npopulation')

#provincial population analysis
provincial_population_data = pd.read_excel ('Provincial projection by sex and age (2002-2020)_web.xlsx', sheet_name = 'Sheet1')

years_range = ['2002', '2003', '2004', '2005', '2006', '2007',
               '2008', '2009', '2010', '2011', '2012', '2013',
               '2014', '2015', '2016', '2017', '2018', '2019', '2020']

#Calculates and total provincial population per annum (2002 to 2020)
def province_population_increase(first_row, last_row, popul_data):
    increase_list = []
    total_population_yearly = 0
    for year in range(3, 22):
        for i in range (first_row, last_row):
            age_group_total_population_yearly = popul_data.iloc[i, year]
            total_population_yearly += age_group_total_population_yearly/1E6;

        increase_list.append(total_population_yearly)
        total_population_yearly = 0
    return increase_list

#Provincial population analysis (age group and sex distribution)
def provincial_stats_by_sex_and_age (province_row_start, province_row_end, data_of_province):
    population_data_of_province = data_of_province.iloc[province_row_start:province_row_end, 0:22]
    population_data_of_province.columns = ['Name', 'Sex', 'Age',
                                            2002, 2003, 2004, 2005, 2006, 2007,
                                            2008, 2009, 2010, 2011, 2012, 2013,
                                            2014, 2015, 2016, 2017, 2018, 2019, 2020]

    province_population_by_sex_and_age = population_data_of_province.iloc[1:35, [0, 1, 2, 21]]
    PROVINCE_MALE_POPULATION = province_population_by_sex_and_age.iloc[0:17, [2, 3]]
    PROVINCE_FEMALE_POPULATION = province_population_by_sex_and_age.iloc[17:34, [2, 3]]
    for x in range(17):
        PROVINCE_MALE_POPULATION.iloc[x, 1] = PROVINCE_MALE_POPULATION.iloc[x, 1]/1E3
        PROVINCE_FEMALE_POPULATION.iloc[x, 1] = PROVINCE_FEMALE_POPULATION.iloc[x, 1]/1E3
    return {'PROVINCE_MALE_POPULATION':PROVINCE_MALE_POPULATION, 'PROVINCE_FEMALE_POPULATION': PROVINCE_FEMALE_POPULATION}

#Analysis of eastern cape population data
eastern_cape_population_data = provincial_population_data.iloc[3:38, 0:22]

E_CAPE_POPUL_BY_AGE_AND_SEX = provincial_stats_by_sex_and_age (province_row_start = 3, province_row_end = 38, data_of_province = provincial_population_data)

E_CAPE_MALE_POPULATION = E_CAPE_POPUL_BY_AGE_AND_SEX['PROVINCE_MALE_POPULATION']
E_CAPE_FEMALE_POPULATION = E_CAPE_POPUL_BY_AGE_AND_SEX['PROVINCE_FEMALE_POPULATION']

E_CAPE_MALE_POPULATION.columns = ['Age', 'Population \n(Thousand)']
E_CAPE_FEMALE_POPULATION.columns = ['Age', 'Poulation \n(Thousand)']

fig, (ax_2, ax2_2) = plt.subplots(ncols=2, sharey=True)
ax_2.invert_xaxis()
ax_2.yaxis.tick_right()

E_CAPE_MALE_POPULATION.plot.barh(ax = ax_2, color = '#40cfcc', title = 'Age distribution of\n Eastern Cape male \npopulation')
E_CAPE_FEMALE_POPULATION.plot.barh(x = 'Age', ax = ax2_2, color = '#40cfcc', title = 'Age distribution of\n Eastern Cape female \npopulation')

popul_increase_E_CAPE = province_population_increase(first_row = 1, last_row = 35, popul_data = eastern_cape_population_data)

#create dataframe of population increase and plot it
E_CAPE_DATAFRAME = pd.DataFrame({'Years': years_range, 'increase_data': popul_increase_E_CAPE})
E_CAPE_DATAFRAME_PLOT = E_CAPE_DATAFRAME.plot.bar(x='Years', y='increase_data', rot=90, legend=None,
                          title = 'Eastern Cape population trend (2002 to 2020)', color = '#40cfcc')
E_CAPE_DATAFRAME_PLOT.set_xlabel("Year")
E_CAPE_DATAFRAME_PLOT.set_ylabel("Population (Million)")

print(E_CAPE_FEMALE_POPULATION)
#fig.tight_layout()
fig.subplots_adjust(wspace=0.25)

plt.show()

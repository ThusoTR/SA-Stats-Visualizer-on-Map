import pandas as pd
import matplotlib.pyplot as plt
import datetime
import seaborn as sns

population_data = pd.read_excel ('Country projection by population group, sex and age (2002-2019).xlsx', sheet_name = 'Sheet1')

#select rows and columns that represent population growth
population_growth = population_data.iloc[[3, 140], 3:21]

#set columns in the first row as headings
population_growth.columns = [2002, 2003, 2004, 2005, 2006, 2007,
                             2008, 2009, 2010, 2011, 2012, 2013,
                             2014, 2015, 2016, 2017, 2018, 2019 ]

population_growth = population_growth.iloc[1, 0:21]

#convert population values into int
for x in range(18):
    population_growth.iloc[x] = int(population_growth.iloc[x]/1000000)




population_growth.T.plot.bar()


population_by_sex_and_age = population_data.iloc[4:38, [22, 23, 41]]
population_by_sex_and_age.columns = ['Sex', 'Age', 'Year: 2019']
male_population_by_age = population_by_sex_and_age.iloc[0:17, [1, 2]]
female_population_by_age = population_by_sex_and_age.iloc[17:35, [1, 2]]

# for x in range(18):
#     female_population_by_age.iloc[x] = int(female_population_by_age.iloc[x]/1000000)
#     male_population_by_age.iloc[x] = int(male_population_by_age.iloc[x]/1000000)
#population_by_sex_and_age.groupby('Sex').plot(kind='kde')

fig, (ax, ax2) = plt.subplots(ncols=2, sharey=True)
ax.invert_xaxis()
ax.yaxis.tick_right()

female_population_by_age.plot.barh(ax = ax)
male_population_by_age.plot.barh(x = 'Age', ax = ax2)

plt.show()
#print(female_population_by_age)

#plt.show(block=True);

#provinsial analysis
provinsial_population_data = pd.read_excel ('Provincial projection by sex and age (2002-2020)_web.xlsx', sheet_name = 'Sheet1')

eastern_cape_population_data = provinsial_population_data.iloc[3:38, 0:22]

eastern_cape_population_data.columns = ['Name', 'Sex', 'Age',
                                        2002, 2003, 2004, 2005, 2006, 2007,
                                        2008, 2009, 2010, 2011, 2012, 2013,
                                        2014, 2015, 2016, 2017, 2018, 2019, 2020]
eastern_cape_population_by_sex_and_age = eastern_cape_population_data.iloc[0:5, 21]
print(eastern_cape_population_by_sex_and_age)

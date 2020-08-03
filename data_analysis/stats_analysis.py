import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-whitegrid")

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
plt.subplots_adjust(left=None, bottom= 0.25, right= None, top=None, wspace=None, hspace=None)
plt.savefig('Population Stats/South Africa population trends (2002 to 2020).png', format='png', dpi=600)

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
fig.savefig('Population Stats/Population Distrion By Age and Sex.png', format='png', dpi=600)

#S.A popuplation report tables

#population by age group
SA_POP_BY_GRP_AND_SEX = pd.read_excel ('MYPE report table website_ 2020.xlsx', sheet_name = 'MYPE by pop grp and sex')
SA_POP_BY_GRP_AND_SEX = SA_POP_BY_GRP_AND_SEX.iloc[2:6, 0:7]
SA_POP_BY_GRP_AND_SEX.columns = ['Population Group', 'Total Male Population', '% of Total S.A Male Population',
                                 'Total of Female population', '% of Total S.A female Population', 'Total',
                                 '% of Total S.A Population']

SA_POP_BY_GRP_AND_SEX['Total Male Population'] = SA_POP_BY_GRP_AND_SEX['Total Male Population'].div(1E6)
SA_POP_BY_GRP_AND_SEX['Total of Female population'] = SA_POP_BY_GRP_AND_SEX['Total of Female population'].div(1E6)
SA_POP_BY_GRP_AND_SEX['Total'] = SA_POP_BY_GRP_AND_SEX['Total'].div(1E6)

Plot_Absolute_Val_Of_SA_POP_BY_GRP_AND_SEX = SA_POP_BY_GRP_AND_SEX.iloc[0:4, [0, 1, 3]]
Plot_Absolute_Val_Of_SA_POP_BY_GRP_AND_SEX = Plot_Absolute_Val_Of_SA_POP_BY_GRP_AND_SEX.set_index('Population Group')
Population_Group_Plot = Plot_Absolute_Val_Of_SA_POP_BY_GRP_AND_SEX.plot(kind = 'bar', title = 'Population estimate by sex and race')
Population_Group_Plot.invert_xaxis()
Population_Group_Plot.set_xlabel("Population Group")
Population_Group_Plot.set_ylabel("Population (Million)")
plt.tight_layout()
plt.savefig('Population Stats/Population estimate by sex and race.png', format='png', dpi=600)

Plot_Percentage_Of_SA_POP_BY_GRP_AND_SEX = SA_POP_BY_GRP_AND_SEX.iloc[0:4, [0, 2, 4]]
Plot_Percentage_Of_SA_POP_BY_GRP_AND_SEX = Plot_Percentage_Of_SA_POP_BY_GRP_AND_SEX.set_index('Population Group')
Population_Percentage_Group_Plot = Plot_Percentage_Of_SA_POP_BY_GRP_AND_SEX.plot(kind = 'bar', title = 'Population estimate by sex and race')
Population_Percentage_Group_Plot.invert_xaxis()

Population_Percentage_Group_Plot.set_xlabel("Population Group")
Population_Percentage_Group_Plot.set_ylabel("% Estimate)")
plt.subplots_adjust(left=None, bottom= 0.25, right= None, top=None, wspace=None, hspace=None)
plt.savefig('Population Stats/Percentage_Population estimate by sex and race.png', format='png', dpi=600)

#life expectancy
LIFE_EXPECTANCY_DATA = pd.read_excel ('MYPE report table website_ 2020.xlsx', sheet_name = 'Assumption of LE withoutHIV&TFR')
LIFE_EXPECTANCY_DATA = LIFE_EXPECTANCY_DATA.iloc[1:20, [0, 2, 3]]
LIFE_EXPECTANCY_DATA.columns = ['Year', 'Male', 'Female']
LIFE_EXPECTANCY_DATA['Year'] = LIFE_EXPECTANCY_DATA['Year'].apply(int)
LIFE_EXPECTANCY_DATA['Year'] = LIFE_EXPECTANCY_DATA['Year'].apply(str)
LIFE_EXPECTANCY_DATA = LIFE_EXPECTANCY_DATA.set_index('Year')
LIFE_EXPECTANCY_TREND_PLOT = LIFE_EXPECTANCY_DATA.plot(kind = 'bar',rot= 90,
                                                       title = 'Assumption of life expectancy')

plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
LIFE_EXPECTANCY_TREND_PLOT.set_xlabel("Year")
LIFE_EXPECTANCY_TREND_PLOT.set_ylabel("Life expectancy (Years)")
plt.subplots_adjust(left=None, bottom= 0.23, right= 0.82, top=None, wspace=None, hspace=None)
plt.savefig('Population Stats/Assumption of life expectancy.png', format='png', dpi=600)

#population by province
population_by_province_data = pd.read_excel ('MYPE report table website_ 2020.xlsx', sheet_name = 'MYPE by province')
population_by_province_data = population_by_province_data.iloc[2:11, 1:3]
population_by_province_data.columns = ['Province','Population Estimate']

population_by_province_data['Population Estimate'] = population_by_province_data['Population Estimate'].div(1E6)

population_by_province_data = population_by_province_data.set_index('Province')
population_by_province_plot = population_by_province_data.plot(kind = 'bar',rot= 90, width=0.25)

population_by_province_plot.set_xlabel("Province")
population_by_province_plot.set_ylabel("Population (Million)")
plt.subplots_adjust(left=None, bottom= 0.30, right= None, top=None, wspace=None, hspace=None)
plt.savefig('Population Stats/population_by_province_plot.png', format='png', dpi=600)

#International net migration
net_migration_data = pd.read_excel ('MYPE report table website_ 2020.xlsx', sheet_name = 'International Net migration')
net_migration_data = net_migration_data.iloc[0:5, 1:6]
net_migration_data = net_migration_data.rename(columns = {'Unnamed: 1':'Period'})

net_migration_data['African'] = net_migration_data['African'].div(1E3)
net_migration_data['Indian/Asian'] = net_migration_data['Indian/Asian'].div(1E3)
net_migration_data['White'] = net_migration_data['White'].div(1E3)
net_migration_data['Net Internationl Migration'] = net_migration_data['Net Internationl Migration'].div(1E3)

net_migration_data = net_migration_data.set_index('Period')
net_migration_plot = net_migration_data.plot(kind = 'bar', rot= 65,
                                             title = 'International Net migration')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
net_migration_plot.set_xlabel("Period")
net_migration_plot.set_ylabel("Net Migration (Thousand)")
plt.subplots_adjust(left=None, bottom= 0.23, right= 0.61, top=None, wspace=None, hspace=None)
plt.savefig('Population Stats/International Net migration.png', format='png', dpi=600)

#Births and deaths over time
Births_and_deaths_data = pd.read_excel ('MYPE report table website_ 2020.xlsx', sheet_name = 'Births and deaths over time')
Births_and_deaths_data.columns = ['Year', 'Number of Births', 'Number of deaths', 'Number of AIDS related deaths', 'Percentage of AIDS related deaths']
Births_and_deaths_data = Births_and_deaths_data.iloc[1:20, 0:5]
Births_and_deaths_data = Births_and_deaths_data.rename(columns = {'nan':'Year'})
Births_and_deaths_data['Year'] = Births_and_deaths_data['Year'].apply(int)
Births_and_deaths_data['Year'] = Births_and_deaths_data['Year'].apply(str)

AIDS_related_deaths = Births_and_deaths_data.iloc[1:20, [0, 4]]
Births_and_deaths_data = Births_and_deaths_data.iloc[1:20, 0:4]

Births_and_deaths_data['Number of Births'] = Births_and_deaths_data['Number of Births'].div(1000)
Births_and_deaths_data['Number of AIDS related deaths'] = Births_and_deaths_data['Number of AIDS related deaths'].div(1000)
Births_and_deaths_data['Number of deaths'] = Births_and_deaths_data['Number of deaths'].div(1000)

Births_and_deaths_data = Births_and_deaths_data.set_index('Year')
Births_and_deaths_plot = Births_and_deaths_data.plot(kind = 'bar', rot= 90,
                                                     title = "Births and deaths over time")
Births_and_deaths_plot.set_xlabel("Year")
Births_and_deaths_plot.set_ylabel("Briths and deaths (Thousand)")
Births_and_deaths_plot.set_ylim(0,1600)
#plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.subplots_adjust(left=None, bottom= 0.15, right=None, top=None, wspace=None, hspace=None)
plt.savefig('Population Stats/Births and deaths over time.png', format='png', dpi=600)

#percentage of AIDS related deaths
AIDS_related_deaths = AIDS_related_deaths.set_index('Year')
AIDS_related_deaths_plot = AIDS_related_deaths.plot(kind = 'bar', rot= 90,
                                                    title = "AIDS related deaths per annum")
AIDS_related_deaths_plot.set_xlabel("Year")
AIDS_related_deaths_plot.set_ylabel("% of total deathts")
plt.subplots_adjust(left=None, bottom= 0.23, right= None, top=None, wspace=None, hspace=None)
plt.savefig('Population Stats/AIDS related deaths per annum.png', format='png', dpi=600)

########################################################################################################################################
########################################################################################################################################
########################################################################################################################################

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

def generate_provinsial_data (first_row, last_row, title_plot_male, female_plot_tile, title_population_trend):
    PROVINCE_POPUL_BY_AGE_AND_SEX = provincial_stats_by_sex_and_age (province_row_start = first_row,
                                    province_row_end = last_row, data_of_province = provincial_population_data)
    MALE_POPULATION_OF_PROVINCE = PROVINCE_POPUL_BY_AGE_AND_SEX['PROVINCE_MALE_POPULATION']
    FEMALE_POPULATION_OF_PROVINCE = PROVINCE_POPUL_BY_AGE_AND_SEX['PROVINCE_FEMALE_POPULATION']

    MALE_POPULATION_OF_PROVINCE.columns = ['Age', 'Population \n(Thousand)']
    FEMALE_POPULATION_OF_PROVINCE.columns = ['Age', 'Poulation \n(Thousand)']

    fig, (ax_2, ax2_2) = plt.subplots(ncols=2, sharey=True)
    #ax2_2.set_xlim(0,500)
    ax_2.invert_xaxis()
    ax_2.yaxis.tick_right()
    fig.subplots_adjust(wspace=0.25)
    print(MALE_POPULATION_OF_PROVINCE)
    #Visualization population trend data of province
    MALE_POPULATION_OF_PROVINCE.plot.barh(ax = ax_2, color = '#40cfcc',
                                          title = title_plot_male)
    FEMALE_POPULATION_OF_PROVINCE.plot.barh(x = 'Age', ax = ax2_2, color = '#40cfcc',
                                            title = female_plot_tile)
    fig.tight_layout()
    save_path = 'Population Stats/Provincial/' + female_plot_tile.split('\n')[0] + '_Trends.png'
    plt.savefig(save_path, format='png', dpi=600)

    province_population_trend_data = provincial_population_data.iloc[first_row:last_row, 0:22]
    population_increase_of_province = province_population_increase(first_row = 1, last_row = 35, popul_data = province_population_trend_data)

    #create dataframe of population increase and plot it
    PROVINCE_DATAFRAME = pd.DataFrame({'Years': years_range, 'increase_data': population_increase_of_province})
    PROVINCE_DATAFRAME_PLOT = PROVINCE_DATAFRAME.plot.bar(x='Years', y='increase_data', rot=90, legend=None,
                                                        title = title_population_trend, color = '#40cfcc')
    PROVINCE_DATAFRAME_PLOT.set_xlabel("Year")
    PROVINCE_DATAFRAME_PLOT.set_ylabel("Population (Million)")

    save_path = 'Population Stats/Provincial/' + title_population_trend + '_Trends.png'
    plt.savefig(save_path, format='png', dpi=600)

    return {'increase_of_population_province': PROVINCE_DATAFRAME_PLOT,
            'population_by_age_group_province': fig}

#Analysis of provincial population data
E_CAPE_first_row = 3
last_row_E_CAPE = 38
male_E_CAPE_title_plot = 'Eastern Cape male \npopulation by\n age group'
E_CAPE_title_plot_female = 'Eastern Cape female \npopulation by\n age group'
title_population_trend_E_CAPE = 'Eastern Cape population trend (2002 to 2020)'

Eastern_Cape_Plots = generate_provinsial_data (E_CAPE_first_row, last_row_E_CAPE, male_E_CAPE_title_plot,
                          E_CAPE_title_plot_female, title_population_trend_E_CAPE)

FREE_STATE_first_row = 37
last_row_FREE_STATE = 72
male_FREE_STATE_title_plot = 'Free State male \npopulation by\n age group'
FREE_STATE_title_plot_female = 'Free State female \npopulation by\n age group'
title_population_trend_FREE_STATE = 'Free State population trend (2002 to 2020)'

generate_provinsial_data (FREE_STATE_first_row, last_row_FREE_STATE, male_FREE_STATE_title_plot,
                          FREE_STATE_title_plot_female, title_population_trend_FREE_STATE)

GAUTENG_first_row = 71
last_row_GAUTENG = 106
male_GAUTENG_first_row_title_plot = 'Gauteng male \npopulation by\n age group'
GAUTENG_first_row_title_plot_female = 'Gauteng female \npopulation by\n age group'
title_population_trend_GAUTENG = 'Gauteng population trend (2002 to 2020)'

generate_provinsial_data (GAUTENG_first_row, last_row_GAUTENG, male_GAUTENG_first_row_title_plot,
                          GAUTENG_first_row_title_plot_female, title_population_trend_GAUTENG)

KZN_first_row = 105
last_row_KZN = 140
male_KZN_first_row_title_plot = 'Kwazulu-Natal male \npopulation by\n age group'
KZN_first_row_title_plot_female = 'Kwazulu-Natal \npopulation by\n age group'
title_population_trend_KZN = 'KwaZulu-Natal population trend (2002 to 2020)'

generate_provinsial_data (KZN_first_row, last_row_KZN, male_KZN_first_row_title_plot,
                          KZN_first_row_title_plot_female, title_population_trend_KZN)

LIMPOPO_first_row = 139
last_row_LIMPOPO = 174
male_LIMPOPO_first_row_title_plot = 'Limpopo male \npopulation by\n age group'
LIMPOPO_first_row_title_plot_female = 'Limpopo female \npopulation by\n age group'
title_population_trend_LIMPOPO = 'Limpopo population trend (2002 to 2020)'

generate_provinsial_data (LIMPOPO_first_row, last_row_LIMPOPO, male_LIMPOPO_first_row_title_plot,
                          LIMPOPO_first_row_title_plot_female, title_population_trend_LIMPOPO)

MPUMALANGA_first_row = 173
last_row_MPUMALANGA = 208
male_MPUMALANGA_first_row_title_plot = 'Mpumalanga male \npopulation by\n age group'
MPUMALANGA_first_row_title_plot_female = 'Mpumalanga female \npopulation by\n age group'
title_population_trend_MPUMALANGA = 'Mpumalanga population trend (2002 to 2020)'

generate_provinsial_data (MPUMALANGA_first_row, last_row_MPUMALANGA, male_MPUMALANGA_first_row_title_plot,
                          MPUMALANGA_first_row_title_plot_female, title_population_trend_MPUMALANGA)

N_CAPE_first_row = 207
last_row_N_CAPE = 242
male_N_CAPE_first_row_title_plot = 'Northern Cape male \npopulation by\n age group'
N_CAPE_first_row_title_plot_female = 'Northern Cape female \npopulation by\n age group'
title_population_trend_N_CAPE = 'Northern Cape population trend (2002 to 2020)'

generate_provinsial_data (N_CAPE_first_row, last_row_N_CAPE, male_N_CAPE_first_row_title_plot,
                          N_CAPE_first_row_title_plot_female, title_population_trend_N_CAPE)

N_WEST_first_row = 241
last_row_N_WEST = 276
male_N_WEST_first_row_title_plot = 'North West male \npopulation by\n age group'
N_WEST_first_row_title_plot_female = 'North West female \npopulation by\n age group'
title_population_trend_N_WEST = 'North West population trend (2002 to 2020)'

generate_provinsial_data (N_WEST_first_row, last_row_N_WEST, male_N_WEST_first_row_title_plot,
                          N_WEST_first_row_title_plot_female, title_population_trend_N_WEST)

W_CAPE_first_row = 275
last_row_W_CAPE = 310
male_W_CAPE_first_row_title_plot = 'Western Cape male \npopulation by\n age group'
W_CAPE_first_row_title_plot_female = 'Western Cape female \npopulation by\n age group'
title_population_trend_W_CAPE = 'Western Cape population trend (2002 to 2020)'

generate_provinsial_data (W_CAPE_first_row, last_row_W_CAPE, male_W_CAPE_first_row_title_plot,
                          W_CAPE_first_row_title_plot_female, title_population_trend_W_CAPE)

plt.show()

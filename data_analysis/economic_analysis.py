import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

Working_Age_Population = pd.read_excel ('QLFS Trends 2008-2020Q1.xlsx', sheet_name = 'Table1')
Working_Age_Population.columns = Working_Age_Population.iloc[0]

working_columns = [*range(0,52, 4)]
_columns_ = ['Popuplation Group', 'March 2020']
SA_Working_Age = Working_Age_Population.iloc[7:12, [0, 49]]
SA_Working_Age.iloc[0, 0] = 'S.A Total'
SA_Working_Age.columns = _columns_
SA_Working_Age['March 2020'] = SA_Working_Age['March 2020'].div(1000)
SA_Working_Age = SA_Working_Age.set_index('Popuplation Group')
SA_Working_Age_Plot = SA_Working_Age.plot(kind = 'bar', rot= 65,
                        title = "S.A working age population per population group (15-64 years)")

#SA_Working_Age_Plot.set_xlabel("Population Group")
SA_Working_Age_Plot.set_ylabel("Working Age Population (Million)")
#plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.subplots_adjust(left=None, bottom= 0.22, right=None, top=None, wspace=None, hspace=None)
plt.savefig('Economic Stats/SA Working Age Population.png', format='png', dpi=600)

#Working age population by province
SA_Working_Age_By_Province = Working_Age_Population.iloc[14:23, [0, 49]]
SA_Working_Age_By_Province.columns = ['Province', 'March 2020']

SA_Working_Age_By_Province['March 2020'] = SA_Working_Age_By_Province['March 2020'].div(1000)
SA_Working_Age_By_Province = SA_Working_Age_By_Province.set_index('Province')
SA_Working_Age_By_Province_Plot = SA_Working_Age_By_Province.plot(kind = 'bar', rot= 90,
                                title = "S.A working age population per province (15-64 years)")

#SA_Working_Age_Plot.set_xlabel("Population Group")
SA_Working_Age_By_Province_Plot.set_ylabel("Working Age Population (Million)")
#plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.subplots_adjust(left=None, bottom= 0.26, right=None, top=None, wspace=None, hspace=None)
plt.savefig('Economic Stats/SA Provine Working Age Population.png', format='png', dpi=600)

#Unemployment analysis
Employment_Data = pd.read_excel ('QLFS Trends 2008-2020Q1.xlsx', sheet_name = 'Table 2')
Employment_Data.columns = Employment_Data.iloc[0]
working_columns.append(int(49))
Unmeployment_Trend_Data = Employment_Data.iloc[16:17, working_columns]
Unmeployment_Trend_Data = Unmeployment_Trend_Data.iloc[0:1, 1:]
# Unmeployment_Trend_Data = []
Unmeployment_Trend_Plot = Unmeployment_Trend_Data.T.plot(kind = 'bar', rot = 80,
                                                         title = 'S.A Unemployment - Narrow definition of unemployment')
plt.gca().get_legend().remove()
Unmeployment_Trend_Plot.set_xlabel("Period")
Unmeployment_Trend_Plot.set_ylabel("Unemployment rate(%)")
plt.subplots_adjust(left=None, bottom= 0.28, right=None, top=None, wspace=None, hspace=None)
plt.savefig('Economic Stats/S.A Unemployment_Narrow Definition.png', format='png', dpi=600)
#Expanded definition of emploment South Africa

Expaned_Employment_Data = pd.read_excel ('QLFS Trends 2008-2020Q1.xlsx', sheet_name = 'Table 2.4')
Expaned_Employment_Data.columns = Expaned_Employment_Data.iloc[0]
Both_Sexes = Expaned_Employment_Data.iloc[[4,5,6,11,12], [0, 49]]
Both_Sexes.columns = ['Specification', 'Jan-Mar 2020']

Both_Sexes['Jan-Mar 2020'] = Both_Sexes['Jan-Mar 2020'].div(1000)
Both_Sexes = Both_Sexes.set_index('Specification')
Plot_Both_Sexes = Both_Sexes.plot(kind = 'bar', rot = 65,
                                  title = ' Labour force characteristics of South Africa')
Plot_Both_Sexes.set_ylabel("Population (Million)")
plt.tight_layout()
plt.savefig('Economic Stats/Labour force characteristics of South Africa.png', format='png', dpi=600)
#Male labour force characteristics of South Africa

Male_Labour_Characteristics = Expaned_Employment_Data.iloc[[34,35,36,41,42], [0, 49]]
Male_Labour_Characteristics.columns = ['Specification', 'Jan-Mar 2020']

Male_Labour_Characteristics['Jan-Mar 2020'] = Male_Labour_Characteristics['Jan-Mar 2020'].div(1000)
Male_Labour_Characteristics = Male_Labour_Characteristics.set_index('Specification')
Plot_Male_Labour_Characteristics = Male_Labour_Characteristics.plot(kind = 'bar', rot = 65,
                                  title = ' Male labour force characteristics of South Africa')
Plot_Male_Labour_Characteristics.set_ylabel("Population (Million)")
plt.tight_layout()
plt.savefig('Economic Stats/Male labour force characteristics.png', format='png', dpi=600)

#women

Women = Expaned_Employment_Data.iloc[[19,20,21,26,27], [0, 49]]
Women.columns = ['Specification', 'Jan-Mar 2020']

Women['Jan-Mar 2020'] = Women['Jan-Mar 2020'].div(1000)
Women = Women.set_index('Specification')
Plot_Women = Women.plot(kind = 'bar', rot = 65,
                                  title = ' Female labour force characteristics of South Africa')
Plot_Women.set_ylabel("Population (Million)")
plt.subplots_adjust(left=None, bottom= 0.39, right=None, top=None, wspace=None, hspace=None)
#Provincial economic analysis
Provincial_Employment_Data = pd.read_excel ('QLFS Trends 2008-2020Q1.xlsx', sheet_name = 'Table 2.7')
Provincial_Employment_Data.columns = Provincial_Employment_Data.iloc[0]
plt.tight_layout()
plt.savefig('Economic Stats/Female labour force characteristics.png', format='png', dpi=600)

def provincial_unemploment_trends(list_rows, column_list, title_province, province_name) :

    province_Trend_Data = Provincial_Employment_Data.iloc[list_rows, column_list]
    province_Trend_Data = province_Trend_Data.iloc[0:1, 1:]
    # Unmeployment_Trend_Data = []
    province_Trend_Plot = province_Trend_Data.T.plot(kind = 'bar', rot = 80, title = title_province)
    plt.gca().get_legend().remove()
    province_Trend_Plot.set_xlabel("Period")
    province_Trend_Plot.set_ylabel("Unemployment rate(%)")
    plt.subplots_adjust(left=None, bottom= 0.28, right=None, top=None, wspace=None, hspace=None)
    save_path = 'Economic Stats/' + province_name + '_unemployment_trends.png'
    plt.savefig(save_path, format='png', dpi=600)

#Unemployment per province

unemployment_per_province = Provincial_Employment_Data.iloc[[10, 21, 54, 98, 109, 150, 183, 194, 249, 260], [0, 49]]
unemployment_per_province.columns = ['Unemployment Per Province', 'Unemployment Rate']
unemployment_per_province.iloc[0, 0] = "S.A Average"
unemployment_per_province.iloc[1, 0] = "Western Cape"
unemployment_per_province.iloc[2, 0] = "Eastern Cape"
unemployment_per_province.iloc[3, 0] = "Northen Cape"
unemployment_per_province.iloc[4, 0] = "Free State"
unemployment_per_province.iloc[5, 0] = "Kwazulu-Natal"
unemployment_per_province.iloc[6, 0] = "North West"
unemployment_per_province.iloc[7, 0] = "Gauteng"
unemployment_per_province.iloc[8, 0] = "Mpumalanga"
unemployment_per_province.iloc[9, 0] = "Limpopo"
unemployment_per_province = unemployment_per_province.set_index('Unemployment Per Province')

plot_unemployment_per_province = unemployment_per_province.plot(kind = 'bar', rot = 90,
                                                                title = 'Unemployment per province - Expanded \ndefinition of unemployment')

plot_unemployment_per_province.set_xlabel("South African Province")
plot_unemployment_per_province.set_ylabel("Unemployment rate(%)")
# plt.subplots_adjust(left=None, bottom= 0.28, right=None, top=None, wspace=None, hspace=None)

plt.tight_layout()
plt.savefig('Economic Stats/Unemployment per province_Expanded.png', format='png', dpi=600)

#Labour force characteristics - Expanded definition of unemployment
SA_rows = slice(10, 11)
SA_columns = working_columns
SA_title = 'South Africa: Labour force characteristics - Expanded \ndefinition of unemployment'
provincial_unemploment_trends(list_rows = SA_rows, column_list = SA_columns,
                              title_province = SA_title, province_name = "South Africa")

western_cape_rows = slice(21, 22)
western_cape_columns = working_columns
western_cape_title = 'Western Cape: Labour force characteristics - Expanded \ndefinition of unemployment'
provincial_unemploment_trends(list_rows = western_cape_rows, column_list = western_cape_columns,
                              title_province = western_cape_title, province_name = "Western Cape")

E_cape_rows = slice(54, 55)
E_cape_columns = working_columns
E_cape_title = 'Eastern Cape: Labour force characteristics - Expanded \ndefinition of unemployment'
provincial_unemploment_trends(list_rows = E_cape_rows, column_list = E_cape_columns,
                              title_province = E_cape_title, province_name = "Eastern Cape")

N_cape_rows = slice(98, 99)
N_cape_columns = working_columns
N_cape_title = 'Northern Cape: Labour force characteristics - Expanded \ndefinition of unemployment'
provincial_unemploment_trends(list_rows = N_cape_rows, column_list = N_cape_columns,
                              title_province = N_cape_title, province_name = "Northern Cape")

Free_State_rows = slice(109, 110)
Free_State_columns = working_columns
Free_State_title = 'Free State: Labour force characteristics - Expanded \ndefinition of unemployment'
provincial_unemploment_trends(list_rows = Free_State_rows, column_list = Free_State_columns,
                              title_province = Free_State_title, province_name = "Free State")

KZN_rows = slice(150, 151)
KZN_columns = working_columns
KZN_title = 'Kwazulu-Natal: Labour force characteristics - Expanded \ndefinition of unemployment'
provincial_unemploment_trends(list_rows = KZN_rows, column_list = KZN_columns,
                              title_province = KZN_title, province_name = "Kwazulu-Natal")

North_West_rows = slice(183, 184)
North_West_columns = working_columns
North_West_title = 'North West: Labour force characteristics - Expanded \ndefinition of unemployment'
provincial_unemploment_trends(list_rows = North_West_rows, column_list = North_West_columns,
                              title_province = North_West_title, province_name = "North West")

GP_rows = slice(194, 195)
GP_columns = working_columns
GP_title = 'Gauteng: Labour force characteristics - Expanded \ndefinition of unemployment'
provincial_unemploment_trends(list_rows = GP_rows, column_list = GP_columns,
                              title_province = GP_title, province_name = "Gauteng")


MP_rows = slice(249, 250)
MP_columns = working_columns
MP_title = 'Mpumalanga: Labour force characteristics - Expanded \ndefinition of unemployment'
provincial_unemploment_trends(list_rows = MP_rows, column_list = MP_columns,
                              title_province = MP_title, province_name = "North West")

LP_rows = slice(260, 261)
LP_columns = working_columns
LP_title = 'Limpopo: Labour force characteristics - Expanded \ndefinition of unemployment'
provincial_unemploment_trends(list_rows = LP_rows, column_list = LP_columns,
                              title_province = LP_title, province_name = "Limpopo")

unemployment_by_age_group = pd.read_excel ('QLFS Trends 2008-2020Q1.xlsx', sheet_name = 'Table 2.6')

unemployment_by_age_group = unemployment_by_age_group.iloc[[10, 21, 32, 43, 54, 65], [0, 49]]
unemployment_by_age_group.columns = ['Unemployment By Age Group', 'Unemployment Rate']
unemployment_by_age_group.iloc[0, 0] = "S.A Average"
unemployment_by_age_group.iloc[1, 0] = "15-24 Years"
unemployment_by_age_group.iloc[2, 0] = "25-34 Years"
unemployment_by_age_group.iloc[3, 0] = "35-44 Years"
unemployment_by_age_group.iloc[4, 0] = "45-54 Years"
unemployment_by_age_group.iloc[5, 0] = "55-64 Years"
unemployment_by_age_group = unemployment_by_age_group.set_index('Unemployment By Age Group')

plot_unemployment_by_age_group = unemployment_by_age_group.plot(kind = 'bar', rot = 90,
                                                                title = 'Unemployment by age group - Expanded \ndefinition of unemployment')

plot_unemployment_by_age_group.set_xlabel("Age Group")
plot_unemployment_by_age_group.set_ylabel("Unemployment rate(%)")
# plt.subplots_adjust(left=None, bottom= 0.28, right=None, top=None, wspace=None, hspace=None)

plt.tight_layout()
plt.savefig('Economic Stats/Unemployment by age group_Expanded.png', format='png', dpi=600)

print(unemployment_by_age_group)

#Unemployment per population Group
unemployment_by_population_group = pd.read_excel ('QLFS Trends 2008-2020Q1.xlsx', sheet_name = 'Table 2.5')

unemployment_by_population_group = unemployment_by_population_group.iloc[[10, 21, 32, 43, 54], [0, 49]]
unemployment_by_population_group.columns = ['Unemployment Per Population Group', 'Unemployment Rate']
unemployment_by_population_group.iloc[0, 0] = "S.A Average"
unemployment_by_population_group.iloc[1, 0] = "Black/African"
unemployment_by_population_group.iloc[2, 0] = "Coloured"
unemployment_by_population_group.iloc[3, 0] = "Indian/Asian"
unemployment_by_population_group.iloc[4, 0] = "White"

unemployment_by_population_group = unemployment_by_population_group.set_index('Unemployment Per Population Group')

plot_unemployment_by_population_group = unemployment_by_population_group.plot(kind = 'bar', rot = 90,
                                                                title = 'Unemployment per population group - Expanded \ndefinition of unemployment')

plot_unemployment_by_population_group.set_xlabel("Population Group")
plot_unemployment_by_population_group.set_ylabel("Unemployment rate(%)")
# plt.subplots_adjust(left=None, bottom= 0.28, right=None, top=None, wspace=None, hspace=None)

plt.tight_layout()
plt.savefig('Economic Stats/Unemployment per population group_Expanded.png', format='png', dpi=600)

# plt.show()

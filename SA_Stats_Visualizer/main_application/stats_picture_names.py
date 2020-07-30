#South Africa Stats: Picture provincial_unemploment_trends
def province_names():
    province_names = {
        'Gauteng': 'Gauteng',
        'Eastern_Cape': 'Eastern Cape',
        'Kwazulu-Natal': 'Kwazulu-Natal',
        'Limpopo': 'Limpopo',
        'Free State': 'Free State',
        'Western Cape': 'Western Cape',
        'Northern Cape': 'Northern Cape',
        'Mpumalanga': 'Mpumalanga',
        'North West': 'North West'

    }
    return province_names

def SA_PICTURES_AND_STATS_VALUES():
    South_Africa_Stats_Dict = {
        'Assumption': "main_application/Population Stats/Assumption of life expectancy.png",
        'population_per_province': "main_application/Population Stats/population_by_province_plot.png",
        'AIDS_related_deaths': "main_application/Population Stats/AIDS related deaths per annum.png",
        'International_Net_migration': "main_application/Population Stats/International Net migration.png",
        'Percentage_Population_estimate_by_sex_and_race': "main_application/Population Stats/Percentage_Population estimate by sex and race.png",
        'Population_Distrion_By_Age_and_Sex': "main_application/Population Stats/Population Distrion By Age and Sex.png",
        'South_Africa_population_trends': "main_application/Population Stats/South Africa population trends (2002 to 2020).png",
        'Births_and_deaths_over_time': "main_application/Population Stats/Births and deaths over time.png",

        'GDP_Growth': 'main_application/Economic Stats/GDP Growth.png',
        'SA_Provine_Working_Age_Population': 'main_application/Economic Stats/SA Provine Working Age Population.png',
        'SA_Working_Age_Population': 'main_application/Economic Stats/SA Working Age Population.png',
        'SA_Unemployment_Narrow_Definition': 'main_application/Economic Stats/S.A Unemployment_Narrow Definition.png',
        'South_Africa_unemployment_trends': 'main_application/Economic Stats/South Africa_unemployment_trends.png',
        'Unemployment_by_age_group_Expanded': 'main_application/Economic Stats/Unemployment by age group_Expanded.png',
        'Unemployment_per_population_group': 'main_application/Economic Stats/Unemployment per population group_Expanded.png',
        'Unemployment_per_province_Expanded': 'main_application/Economic Stats/Unemployment per province_Expanded.png',
        }
    return South_Africa_Stats_Dict;

def PROVINCIAL_PICTURES_AND_STATS_VALUES(province_name):
    Eastern_Stats_Dict = {
        'population_by_sex_and_age': "main_application/Population Stats/Provincial/Eastern Cape female _Trends.png",
        'population_trends': "main_application/Population Stats/Provincial/Eastern Cape population trend (2002 to 2020)_Trends.png",
        'unemployment_trends': "main_application/Economic Stats/Eastern Cape_unemployment_trends.png",

        'population_2002': '6.5 million',
        'population_2020': '6.7 million',
        'unemployed_2002': '36 %',
        'unemployed_2020': '49 %',
        'working_age_population': '4.3 million',
        'employed': '1.4 million',
        'unemployed': '1.3 million',
        'not_economically_active': '1.6 million',

        'name_of_province': 'Eastern Cape',
        'contribution_to_gdp': '8 %',
        'contribution_to_SA_population': '11.3 %'
    }
    Free_State_Stats_Dict = {
        'population_by_sex_and_age': "main_application/Population Stats/Provincial/Free State female _Trends.png",
        'population_trends': "main_application/Population Stats/Provincial/Free State population trend (2002 to 2020)_Trends.png",
        'unemployment_trends': "main_application/Economic Stats/Free State_unemployment_trends.png",

        'population_2002': '2.7 million',
        'population_2020': '2.9 million',
        'unemployed_2002': '30 %',
        'unemployed_2020': '45 %',
        'working_age_population': '1.9 million',
        'employed': '756 thousand',
        'unemployed': '607 thousand',
        'not_economically_active': '548 thousand',

        'name_of_province': 'Free State',
        'contribution_to_gdp': '5 %',
        'contribution_to_SA_population': '4.9 %'

    }
    Gauteng_Stats_Dict = {
        'population_by_sex_and_age':"main_application/Population Stats/Provincial/Gauteng female _Trends.png",
        'population_trends':"main_application/Population Stats/Provincial/Gauteng population trend (2002 to 2020)_Trends.png",
        'unemployment_trends': "main_application/Economic Stats/Gauteng_unemployment_trends.png",

        'population_2002': '9.7 million',
        'population_2020': '15.5 million',
        'unemployed_2002': '23.4 %',
        'unemployed_2020': '36.3 %',
        'working_age_population': '10.5 million',
        'employed': '5.1 million',
        'unemployed': '2.9 million',
        'not_economically_active': '2.5 million',

        'name_of_province': 'Gauteng',
        'contribution_to_gdp': '34 %',
        'contribution_to_SA_population': '26 %'
    }
    KwaZulu_Natal_Stats_Dict = {
        'population_by_sex_and_age': "main_application/Population Stats/Provincial/Kwazulu-Natal _Trends.png",
        'population_trends': "main_application/Population Stats/Provincial/Kwazulu-Natal population trend (2002 to 2020)_Trends.png",
        'unemployment_trends': "main_application/Economic Stats/Kwazulu-Natal_unemployment_trends.png",

        'population_2002': '9.6 million',
        'population_2020': '11.5 million',
        'unemployed_2002': '30 %',
        'unemployed_2020': '43 %',
        'working_age_population': '7.2 million',
        'employed': '2.7 million',
        'unemployed': '2 million',
        'not_economically_active': '2.5 million',

        'name_of_province': 'Kwazulu-Natal',
        'contribution_to_gdp': '16 %',
        'contribution_to_SA_population': '19.3 %'
    }
    Limpopo_Stats_Dict = {
        'population_by_sex_and_age': "main_application/Population Stats/Provincial/Limpopo female _Trends.png",
        'population_trends': "main_application/Population Stats/Provincial/Limpopo population trend (2002 to 2020)_Trends.png",
        'unemployment_trends': "main_application/Economic Stats/Limpopo_unemployment_trends.png",

        'population_2002': '5.1 million',
        'population_2020': '5.8 million',
        'unemployed_2002': '43 %',
        'unemployed_2020': '44.4 %',
        'working_age_population': '3.8 million',
        'employed': '1.4 million',
        'unemployed': '1.1 million',
        'not_economically_active': '1.3 million',

        'name_of_province': 'Limpopo',
        'contribution_to_gdp': '7 %',
        'contribution_to_SA_population': '9.8 %'
    }
    Mpumalanga_Stats_Dict = {
        'population_by_sex_and_age': "main_application/Population Stats/Provincial/Mpumalanga female _Trends.png",
        'population_trends': "main_application/Population Stats/Provincial/Mpumalanga population trend (2002 to 2020)_Trends.png",
        'unemployment_trends': "main_application/Economic Stats/Mpumalanga_unemployment_trends.png",

        'population_2002': '3.5 million',
        'population_2020': '4.7 million',
        'unemployed_2002': '33.7 %',
        'unemployed_2020': '43.9 %',
        'working_age_population': '2.98 million',
        'employed': '1.2 million',
        'unemployed': '975 thousand',
        'not_economically_active': '759 thousand',

        'name_of_province': 'Mpumalanga',
        'contribution_to_gdp': '8 %',
        'contribution_to_SA_population': '7.8 %'
    }

    North_West_Stats_Dict = {
        'population_by_sex_and_age': "main_application/Population Stats/Provincial/North West female _Trends.png",
        'population_trends': "main_application/Population Stats/Provincial/North West population trend (2002 to 2020)_Trends.png",
        'unemployment_trends': "main_application/Economic Stats/North West_unemployment_trends.png",

        'population_2002': '3.1 million',
        'population_2020': '4.1 million',
        'unemployed_2002': '33.5 %',
        'unemployed_2020': '45.1 %',
        'working_age_population': '2.6 million',
        'employed': '969 thousand',
        'unemployed': '797 thousand',
        'not_economically_active': '864 thousand',

        'name_of_province': 'North West',
        'contribution_to_gdp': '6 %',
        'contribution_to_SA_population': '6.9 %'
}
    Northern_Cape_Stats_Dict = {
        'population_by_sex_and_age': "main_application/Population Stats/Provincial/Northern Cape female _Trends.png",
        'population_trends': "main_application/Population Stats/Provincial/Northern Cape population trend (2002 to 2020)_Trends.png",
        'unemployment_trends': "main_application/Economic Stats/Northern Cape_unemployment_trends.png",

        'population_2002': '1.1 million',
        'population_2020': '1.3 million',
        'unemployed_2002': '27.5 %',
        'unemployed_2020': '40.1 %',
        'working_age_population': '808 thousand',
        'employed': '336 thousand',
        'unemployed': '224 thousand',
        'not_economically_active': '248 thousand',

        'name_of_province': 'Northern Cape',
        'contribution_to_gdp': '2 %',
        'contribution_to_SA_population': '2.2 %'
    }
    Western_Cape_Stats_Dict = {
        'population_by_sex_and_age': "main_application/Population Stats/Provincial/Western Cape female _Trends.png",
        'population_trends': "main_application/Population Stats/Provincial/Western Cape population trend (2002 to 2020)_Trends.png",
        'unemployment_trends': "main_application/Economic Stats/Western Cape_unemployment_trends.png",

        'population_2002': '4.9 million',
        'population_2020': '7 million',
        'unemployed_2002': '19.1 %',
        'unemployed_2020': '24.8 %',
        'working_age_population': '4.7 million',
        'employed': '2.5 million',
        'unemployed': '826 thousand',
        'not_economically_active': '1.4 million',

        'name_of_province': 'Western Cape',
        'contribution_to_gdp': '14 %',
        'contribution_to_SA_population': '11.8 %'
    }
    province_name = province_name.upper()

    if (province_name == 'GAUTENG'):
        return Gauteng_Stats_Dict
    elif(province_name == 'EASTERN CAPE'):
        return Eastern_Stats_Dict
    elif(province_name == 'FREE STATE'):
        return Free_State_Stats_Dict
    elif(province_name == 'MPUMALANGA'):
        return Mpumalanga_Stats_Dict
    elif(province_name == 'WESTERN CAPE'):
        return Western_Cape_Stats_Dict
    elif(province_name == 'KWAZULU-NATAL'):
        return KwaZulu_Natal_Stats_Dict
    elif(province_name == 'NORTHERN CAPE'):
        return Northern_Cape_Stats_Dict
    elif(province_name == 'LIMPOPO'):
        return Limpopo_Stats_Dict
    elif(province_name == 'NORTH WEST'):
        return North_West_Stats_Dict

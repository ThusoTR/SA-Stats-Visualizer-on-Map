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
        'unemployment_trends': "main_application/Economic Stats/Eastern Cape_unemployment_trends.png"
    }
    Free_State_Stats_Dict = {
        'population_by_sex_and_age': "main_application/Economic Stats/Free State Cape female _Trends.png",
        'population_trends': "main_application/Economic Stats/Free State population trend (2002 to 2020)_Trends.png",
        'unemployment_trends': "main_application/Economic Stats/Frees State_unemployment_trends.png"
    }
    Gauteng_Stats_Dict = {
        'population_by_sex_and_age':"main_application/Economic Stats/Gauteng female _Trends.png",
        'population_trends':"main_application/Economic Stats/Gauteng population trend (2002 to 2020)_Trends.png",
        'unemployment_trends': "main_application/Economic Stats/Gauteng_unemployment_trends.png"
    }
    KwaZulu_Natal_Stats_Dict = {
        'population_by_sex_and_age': "main_application/Economic Stats/Kwazulu-Natal_Trends.png",
        'population_trends': "main_application/Economic Stats/Kwazulu-Natal population trend (2002 to 2020)_Trends.png",
        'unemployment_trends': "main_application/Economic Stats/Kwazulu-Natal_unemployment_trends.png"
    }
    Limpopo_Stats_Dict = {
        'population_by_sex_and_age': "main_application/Economic Stats/Limpopo female _Trends.png",
        'population_trends': "main_application/Economic Stats/Limpopo population trend (2002 to 2020)_Trends.png",
        'unemployment_trends': "main_application/Economic Stats/Limpopo_unemployment_trends.png"
    }
    Mpumalanga_Stats_Dict = {
        'population_by_sex_and_age': "main_application/Economic Stats/Mpumalanga female _Trends.png",
        'population_trends': "Mpulamanga population trend (2002 to 2020)_Trends.png",
        'unemployment_trends': "main_application/Economic Stats/Mpumalanga_unemployment_trends.png"
    }

    North_West_Stats_Dict = {
        'population_by_sex_and_age': "main_application/Economic Stats/North West female _Trends.png",
        'population_trends': "main_application/Economic Stats/North West population trend (2002 to 2020)_Trends.png",
        'unemployment_trends': "main_application/Economic Stats/North West_unemployment_trends.png"
    }
    Northern_Cape_Stats_Dict = {
        'population_by_sex_and_age': "main_application/Economic Stats/Northern Cape female _Trends.png",
        'population_trends': "main_application/Economic Stats/Northern Cape population trend (2002 to 2020)_Trends.png",
        'unemployment_trends': "main_application/Economic Stats/Northern Cape_unemployment_trends.png"
    }
    Western_Cape_Stats_Dict = {
        'population_by_sex_and_age': "main_application/Economic Stats/Western Cape female _Trends.png",
        'population_trends': "main_application/Economic Stats/Western Cape population trend (2002 to 2020)_Trends.png",
        'unemployment_trends': "main_application/Economic Stats/Western Cape_unemployment_trends.png"
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

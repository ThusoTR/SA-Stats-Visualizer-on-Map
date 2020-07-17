import pandas as pd
import matplotlib.pyplot as plt

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


#Unemployment analysis
Employment_Data = pd.read_excel ('QLFS Trends 2008-2020Q1.xlsx', sheet_name = 'Table 2')
Employment_Data.columns = Employment_Data.iloc[0]
working_columns.append(int(49))
Unmeployment_Trend_Data = Employment_Data.iloc[16:17, working_columns]
Unmeployment_Trend_Data = Unmeployment_Trend_Data.iloc[0:1, 1:]
# Unmeployment_Trend_Data = []
Unmeployment_Trend_Plot = Unmeployment_Trend_Data.T.plot(kind = 'bar', rot = 80)
plt.gca().get_legend().remove()
Unmeployment_Trend_Plot.set_xlabel("Period")
Unmeployment_Trend_Plot.set_ylabel("Unemployment rate(%)")
plt.subplots_adjust(left=None, bottom= 0.28, right=None, top=None, wspace=None, hspace=None)

print(working_columns)

plt.show()

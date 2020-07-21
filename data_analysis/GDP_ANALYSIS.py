import pandas as pd
import matplotlib.pyplot as plt
from cycler import cycler

plt.rcParams['axes.prop_cycle'] = cycler(color='bgrcmyk')
plt.style.use("ggplot")

GDP_DATA = pd.read_excel ('GDPp 1q20 previous format.xls', sheet_name = 'Table2 ')
GDP_DATA.columns = GDP_DATA.iloc[0]

growth_rows = slice(9, 27)

GDP_GROWTH = GDP_DATA.iloc[growth_rows, [0, 14]]
GDP_GROWTH.columns = ['Year', 'GDP Growth']
GDP_GROWTH = GDP_GROWTH.set_index('Year')
GDP_GROWTH_PLOT = GDP_GROWTH.plot(kind = 'bar', rot = 90)
GDP_GROWTH_PLOT.set_ylabel("Year - on - year GDP growth (%)")
GDP_GROWTH_PLOT.set_xlabel("Year")
plt.tight_layout()
plt.savefig('Economic Stats/GDP Growth.png', format='png', dpi=600)
print(GDP_GROWTH)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn")

GDP_DATA = pd.read_excel ('GDPp 1q20 previous format.xls', sheet_name = 'Table2 ')

#GDP_GROWTH = GDP_DATA
print(GDP_DATA)

import pandas as pd
import seaborn as sns
from scipy import stats

df = pd.read_csv('bolos_vendidos.csv')

slope, intercept, r_value, p_value, std_err = stats.linregress(df['Visitas'],df['Vendas'])

ax = sns.regplot(x="Visitas", y="Vendas", data=df, color='b', 
 line_kws={'label':"y = {0:.2f}x + {1:.2f}".format(slope,intercept)})

ax.legend()
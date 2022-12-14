import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('tour.xlsx')
#print(df)
#plt()
plt.rc('font',size=6)
plt.subplot(2,1,1)
plt.barh(df.loc[:,'도시'],df.loc[:,'가격'])
plt.subplot(2,1,2)
plt.scatter(x= df.loc[:,'거리'], y=df.loc[:,'가격'])
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])
plt.show()


print(df)

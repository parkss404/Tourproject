import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

# 그룹의 성격 
df = pd.read_excel('tour.xlsx')
grouped = df.groupby('type')
mean = grouped.mean()['거리'] 
median = grouped.median()['거리']
min = grouped.min()['거리']
max = grouped.max()['거리']
#std = grouped.std()['거리']
#describe = grouped.describe()['거리']
print('\nmean:\n',mean,end='')
print('\nmedian:\n',median,end='')
#print('\nstd:\n',std,end='')
print('\nmin:\n',min,end='')
print('\nmax:\n',max,end='')
#print('\ndescribe:\n',describe,end='')
Ac = df[df.loc[:,'type'] == 'A'].loc[:,'도시']
Ap = df[df.loc[:,'type'] == 'A'].loc[:,'가격']

Bc = df[df.loc[:,'type'] == 'B'].loc[:,'도시']
Bp = df[df.loc[:,'type'] == 'B'].loc[:,'가격']

Cc = df[df.loc[:,'type'] == 'C'].loc[:,'도시']
Cp = df[df.loc[:,'type'] == 'C'].loc[:,'가격']

Dc = df[df.loc[:,'type'] == 'D'].loc[:,'도시']
Dp = df[df.loc[:,'type'] == 'D'].loc[:,'가격']

title_font = {
    'fontsize': 7,
    'fontweight': 'bold'
}

plt.rc('font',size=5)
plt.subplot(2,2,1)
plt.title('A Group(mean:987/median:1009)',fontdict=title_font )
plt.bar(Ac,Ap)
plt.subplot(2,2,2)
plt.title('B Group(mean:3157/median:3121)',fontdict=title_font )
plt.bar(Bc,Bp)
plt.subplot(2,2,3)
plt.title('C Group(mean:7227/median:7219)',fontdict=title_font )
plt.bar(Cc,Cp)
plt.subplot(2,2,4)
plt.title('D Group(mean:9337/median:9320)',fontdict=title_font )
plt.bar(Dc,Dp)
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])
plt.show()
print(Ac)
print(Ap)
#plt.barh(df.loc['','도시'],df.loc[:,'가격'])

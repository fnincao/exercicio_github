# Evolução do número de artigos publicados na base "Web of Science" com o tópicos "Remote Sensing" + "inland water"
# Data da pesquisa 08/05/2020

import matplotlib.pyplot as plt

num = [1,0,0,2,6,8,7,9,7,7,8,6,2,2,11,8,14,12,27,20,17,25,37,46,37,46,72,77,102,92,100,136,153,46]

ano = [1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,\
       2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]

plt.bar(ano,num, color='blue', align='center', linewidth=1, edgecolor='black')
plt.xlim(1986,2021)
plt.xticks(ano,rotation=90, size=6)
plt.yticks([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160], size=6)
plt.xlabel('Ano de Publicação')
plt.ylabel('Número de publicações')
plt.title('Evolução de publicações científicas para tópicos "Remote Sensing" + "Inland Water" \n (Fonte: Web of Science, 08/05/2020)')
plt.grid(b=True, axis='y', linestyle='--', linewidth=0.5)

plt.show()
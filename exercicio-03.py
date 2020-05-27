import matplotlib.pyplot as plt

populacao = [7016987,7624144,8725413,8558868,8630229,8460995,7717658, \
             6766664,6320568,5692014, 4834995,3902344, 3041035, 2224065, \
             1667372,1090517,668623 ,310759, 114964,  31529, 7247]

idade = [x for x in range(len(populacao))]

plt.figure(figsize=(10,8))
plt.barh(idade, populacao,height=0.6, color='blue',edgecolor='black')
plt.yticks(idade, ['0 a 4 anos', '5 a 9 anos', '10 a 14 anos', '15 a 19 anos', '20 a 24 anos', \
                       '25 a 29 anos','30 a 34 anos', '35 a 39 anos', '40 a 44 anos', '45 a 49 anos', '50 a 54 anos', '55 a 59 anos', '60 a 64 anos', \
                       '65 a 69 anos', '70 a 74 anos', '75 a 79 anos', '80 a 84 anos', '85 a 89 anos', \
                       '90 a 94 anos', '95 a 99 anos', '100 anos ou mais'], fontsize=7)
plt.xticks([x for x in range (0,9000001,1000000)], ['0 M', '1 M', '2 M', '3 M', '4 M', '5 M', '6 M', '7 M', '8 M', '9 M'], fontsize=7)
plt.ylabel('Faixa etária')
plt.xlabel('Número de pessoas (em milhões)')
plt.title('Distribuição da População masculina segundo os grupos de idade – Brasil – 2010 (Fonte: IBGE)')


plt.show()
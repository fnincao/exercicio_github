import matplotlib.pyplot as plt

populacao_m = [7016987,7624144,8725413,8558868,8630229,8460995,7717658, \
             6766664,6320568,5692014, 4834995,3902344, 3041035, 2224065, \
             1667372,1090517,668623 ,310759, 114964,  31529, 7247]

populacao_f = [6779171,7345231,8441348,8432004,8614963,8643419, \
                8026854, 7121915, 6688796, 6141338, 5305407, \
                4373877,3468085,2616745, 2074264, 1472930, 998349, \
                508724, 211594, 66806, 16989]
idade = [x for x in range(len(populacao_m))]

plt.figure(figsize=(14,8))

plt.suptitle('Distribuição da População por sexo segundo os grupos de idade – Brasil – 2010 (Fonte: IBGE)', size=16)

plt.subplot(121)
plt.barh(idade, populacao_m,height=0.6, color='blue',edgecolor='black')
plt.yticks(idade,'', fontsize=5)
plt.xticks([x for x in range (0,9000001,1000000)], ['0 M', '1 M', '2 M', '3 M', '4 M', '5 M', '6 M', '7 M', '8 M', '9 M'], fontsize=7)
plt.xlabel('Número de homens (em milhões)')
plt.grid(b=True, linestyle='--', axis='x')
plt.gca().invert_xaxis()
plt.tick_params(axis='y', left=False, right=True)


plt.subplot(122)
plt.barh(idade, populacao_f,height=0.6, color='pink',edgecolor='black')
plt.yticks(idade, ['0 a 4 anos      ', '5 a 9 anos      ', '10 a 14 anos    ', '15 a 19 anos    ', '20 a 24 anos    ', \
                       '25 a 29 anos    ','30 a 34 anos    ', '35 a 39 anos    ', '40 a 44 anos    ', '45 a 49 anos    ', '50 a 54 anos    ', '55 a 59 anos    ', '60 a 64 anos    ', \
                       '65 a 69 anos    ', '70 a 74 anos    ', '75 a 79 anos    ', '80 a 84 anos    ', '85 a 89 anos    ', \
                       '90 a 94 anos    ', '95 a 99 anos    ', '100 anos ou mais'], fontsize=6)
plt.xticks([x for x in range (0,9000001,1000000)], ['0 M', '1 M', '2 M', '3 M', '4 M', '5 M', '6 M', '7 M', '8 M', '9 M'], fontsize=7)
plt.xlabel('Número de mulheres (em milhões)')
plt.grid(b=True, linestyle='--', axis='x')



plt.show()
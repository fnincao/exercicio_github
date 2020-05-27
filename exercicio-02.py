import matplotlib.pyplot as plt

populacao = [6779171,7345231,8441348,8432004,8614963,8643419, \
                8026854, 7121915, 6688796, 6141338, 5305407, \
                4373877,3468085,2616745, 2074264, 1472930, 998349, \
                508724, 211594, 66806, 16989]

idade = [x for x in range(len(populacao))]

plt.figure(figsize=(8,6))
plt.bar (idade, populacao, color = "pink", align='center', linewidth=1, edgecolor='black')
plt.xticks(idade, ['0 a 4 anos', '5 a 9 anos', '10 a 14 anos', '15 a 19 anos', '20 a 24 anos', \
                       '25 a 29 anos','30 a 34 anos', '35 a 39 anos', '40 a 44 anos', '45 a 49 anos', '50 a 54 anos', '55 a 59 anos', '60 a 64 anos', \
                       '65 a 69 anos', '70 a 74 anos', '75 a 79 anos', '80 a 84 anos', '85 a 89 anos', \
                       '90 a 94 anos', '95 a 99 anos', '100 anos ou mais'], rotation=20, fontsize=5)
plt.yticks([x for x in range (0,9000001,1000000)], ['0 M', '1 M', '2 M', '3 M', '4 M', '5 M', '6 M', '7 M', '8 M', '9 M'], fontsize=7)
plt.xlabel('Faixa etária')
plt.ylabel('Número de pessoas (em milhões)')
plt.title('Distribuição da População feminina segundo os grupos de idade – Brasil – 2010 (Fonte: IBGE)')
plt.grid(b=True,color='gray', linestyle='--', linewidth=0.2)
plt.show()
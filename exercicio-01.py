import numpy as np

s1 = np.array([168, 398, 451, 337, 186, 232, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,
242, 331, 251, 323, 106, 1055, 170])

s2 = np.array([168, 400, 451, 300, 186, 200, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,
242, 331, 251, 180, 106, 1055, 200])

#cálculo da distância euclidiana
distancia = np.linalg.norm(s1 - s2)

#média pode ser calculada dessa forma, manipulando as matrizes unidimensionais separadamente
med = (s1 + s2)/2

#Ou criando uma matriz 2X1 e criando a média das linhas para cada elemento
s3 = np.array([s1,s2])

media = np.average(s3, axis=0)

#Compara as matrizes e retorna com o máximo
max = np.maximum(s1,s2)

#Compara as matrizes e retorna com mínimo
min = np.minimum(s1,s2)

print(distancia, '\n', media,'\n', med, '\n', max, '\n', min)

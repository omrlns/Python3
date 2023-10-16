#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

#Resposta
#metro = float(input('Digite uma distância em metros: '))
#cm = metro * 100
#mm = metro * 1000
#print('A distância de {} m corresponde a {:.0f} cm e a {:.0f} mm.'.format(metro, cm, mm))

#Upgrade, nova proposta.
#Escreva um programa que leia um valor em metros e o exiba convertido em quilômetro (km), hectômetro (hm), decâmetro (dam), decímetro (dm), centímetro (cm) e milímetro (mm).

medida = float(input('Digite uma distância em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A distância de {} m corresponde as seguintes conversões: \n{:.0f} mm. \n{:.0f} cm. \n{:.0f } dm. \n{} dam. \n{} hm. \n{} km.'.format(medida, mm, cm, dm, dam, hm, km))


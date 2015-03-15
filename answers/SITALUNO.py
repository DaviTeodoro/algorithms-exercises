notas = []
soma = 0
notinser = int(input('Quantas notas vao ser inseridas? ')) #permite ao usuario desidir quantas notas quer incerir
for i in range(notinser):
	i = float(input('Nota: ')) #atualmente notas acima de 10 podem ser inseridas
	notas.append(i)
for i in notas:
	soma += i
media = soma/notinser
if media >= 5:
	print ('Aluno aprovado')
elif media < 5:
	print ('Aluno reprovado')
print (media)

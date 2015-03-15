np = int(input('Say a number: '))
som = 0
for i in range(1,np):
	if np%i == 0:
		print (i),
		som += i 

if som == np:
	print('It is a perfect number!')
else:
	print ('It is not a perfect number')

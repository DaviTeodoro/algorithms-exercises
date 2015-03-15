print("Lets calculate some areas")
print('1 - Square  2 - rect, 3 - triangle, 4 - trapeze')

calc = int(input('Chose a figure: '))


if calc == 1:
	print ('Square')
	l = int(input('Side: '))
	print (l*l)
	
if calc == 2:
	print ('rect')
	l = int(input('Side: '))
	b = int(input('Base: '))
	print (l*b)
	
if calc == 3:
	print ('triangle')
	b = int(input('Base: '))
	h = int(input('height: '))
	print (b*h/2)
	
if calc == 4:
	print ('trapeze')
	b = int(input('Short base: '))
	bm = int(input('Long base: '))
	h = int(input('height: '))
	print (b+bm*h/2)
	

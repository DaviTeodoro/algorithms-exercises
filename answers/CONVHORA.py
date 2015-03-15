sec = int(input("Seconts: "))

h = sec / 3600
m =  (sec - h*3600) / 60 
s = sec - h*3600 - m*60 
print (h,':',m,':',s)

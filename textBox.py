toPrint = ""
width = 5
height = 4
fill = '+'
edge = '#'

for i in range(0, width):
	toPrint += edge
print(toPrint)
for i in range(0, height - 2):
	toPrint = "#"
	for j in range(0, width -2):
		toPrint += fill
	toPrint += "#"
	print(toPrint)
toPrint = ""
for i in range(0, width):
	toPrint += edge
print(toPrint)
	

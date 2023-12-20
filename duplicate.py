x = ["apple","banana","orange","apple"]
y = []
for fruit in x:
	if fruit not in y:
		y.append(fruit)
x = y
print(x)
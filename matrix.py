x = [[2,4],[6,8]]
y = [[1,3],[5,7]]

res = []
for i in range(len(x)):
	row_res = []
	for j in range(len(x[i])):
		row_res.append(x[i][j] + y[i][j])
	res.append(row_res)
print(res)
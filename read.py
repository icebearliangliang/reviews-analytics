data = []
count = 0
sum1 = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('档案读取完了，总共有', len(data), '笔资料')


for d in data:
	length = len(d)
	sum1 = sum1 + length
average = sum1 / len(data)
print('留言的平均长度为', average)

new = []
for d in data:
	if len(d) < 100 :
		new.append(d)
print('一共有', len(new), '笔留言长度小于100')
print(new[0])
print(new[1])

data = []
count = 0
with open('reviews.txt' , 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count= count+1
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取玩了 , 總共有' , len(data),'筆資料' )

print(data[0])

sum_len = 0
for d in data:
	sum_len = sum_len + len(d) 
print ('平均留言長度是', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new),'留言長度小於100')
print(new[0])
print(new[1])

# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d) 
# print('一共有', len(good), '提到good')
# print(good[0])

#進階的寫法
#good = [ d for d in data if 'good' in d]
#print(good)
bad = []
for d in data:
	if 'bad' in d:
		bad.append('bad')
print('一共有', len(bad), '提到bad')


#文字的計數

wc = {} #word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] +=1
		else:
			wc[word] = 1 #新增key
for word in wc:
	if wc[word] > 1000000:
		print(word,wc[word])
print(wc['Alan'])

while True:
	word = input('你想找甚麼字:')	
	if word == '離開':
		break
	if word in wc:
		print(word,'出現過的次數為',wc[word])
	else: 
		print('沒有這個字出現過喔')

print('感謝你的使用')



	


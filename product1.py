# 二維清單
products = []

while True:
	name = input('請輸入商品名稱：')
	if name == "q":
		break
	price = int(input('請輸入商品價格：'))
	products.append([name, price]) #將小清單加入大清單
print(products)

for p in products:
	print(p[0], '的價格是', p[1])


# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: #沒有該檔案也沒關係
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') 
		#字串可以相加和乘法 ，所以要注意型別轉換問題，如果是非字串則要轉換
		#用,區隔是為了存成csv檔，以利彈性使用
		#用換行是為了要儲存便利，避免變成同一行

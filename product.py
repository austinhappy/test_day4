# 二維清單
products = []

while True:
	name = input('請輸入商品名稱：')
	if name == "q":
		break
	price = input('請輸入商品價格：')
	p = [] #小清單
	p.append(name)
	p.append(price)
	# 可簡單成 p = [name, price]，將三個清單寫入
	products.append(p) #將小清單加入大清單
	# 更簡單成 products.append([name], [price])
print(products)

print(products[0][0])
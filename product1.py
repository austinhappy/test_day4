import os # operating system

#讀取檔案
def read_file(file_name):
	products = []
	with open(file_name, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #直接先跳出繼續執行下一個for迴圈
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# 讓使用者輸入商品名稱和價格(新增商品)
def user_input(products):
	while True:
		name = input('請輸入商品名稱：')
		if name == "q":
			break
		price = int(input('請輸入商品價格：'))
		products.append([name, price]) #將小清單加入大清單
	return products

#印出購買
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(file_name, products):
	with open(file_name, 'w', encoding='utf-8') as f: #沒有該檔案也沒關係
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n') 
			#字串可以相加和乘法 ，所以要注意型別轉換問題，如果是非字串則要轉換
			#用,區隔是為了存成csv檔，以利彈性使用
			#用換行是為了要儲存便利，避免變成同一行

def main():
	file_name = "products.csv"
	if os.path.isfile(file_name): # 需要絕對路徑，在同資料夾中搜尋products是否存在
		print('檔案存在')
		products = read_file(file_name)
	else:
		print('找不到檔案...')

	products = user_input(products)
	print_products(products)
	write_file(file_name, products)

main()

#function的終點是單一簡潔，一個function只做一件事情
#refactor重構，資料結構的進化
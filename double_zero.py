import sys
def double_zero(array):
	count = 0
	arrayNew = array.copy()
	for i in range(len(array)):
			if int(array[i]) == 0:
				arrayNew.insert(i + count, 0)   # через метод інсерт, де перше це індекс, а друге значення - елемент який потрібно вставити 
				count += 1
	return arrayNew


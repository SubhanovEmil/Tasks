# Daxil edilmiş natural ədədin sadə olub-olmadığını 
# çıxışa verən proqramın altproqramını (funksiyasını) Python dilində yazın

num = int(input())
counter = 0

for i in range(1, num +1):
    if num % i == 0:
        counter += 1

if counter == 2:
    print("prime")
else :
    print("not prime")
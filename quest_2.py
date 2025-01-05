#2. 3과 5의 배수를 모두 더하기
k=0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        k+=i
print(k)

# 피보나치 수열을 나열하기
def fibo():
    n=0
    while n==0:
      try:
        n=int(input("피보나치 수열을 출력할 때 최댓값을 입력하시오. (최소 1 이상) : "))
      except ValueError, KeyboardInterrupt:
        print("값을 잘못 입력하셨거나 방해문을 넣으셨습니다. 다시 시도해주세요.")
      else:
        if n<1:
          print("잘못된 값을 넣으셨습니다. 다시 시도해주세요.)
    i=0
    j=[]
    while i<=n:
        if len(j)==0:
            j.append(i)
            i+=1
        elif len(j)<3:
            for k in range(0,2):
                j.append(i)
        else:
            i=j[len(j)-1]+j[len(j)-2]
            if i<=n:
                j.append(i)
    for _ in j:
        print(_, end=" ")
fibo()

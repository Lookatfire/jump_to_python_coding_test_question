#1.  구구단 X단 프로그램 만들기
def gugu():
  num=0
  while num==0:
    try:
      num=int(input("구구단을 돌릴 단 수를 입력하세요 : "))
    except ValueError:
      print('잘못된 값을 입력하였습니다. 다시 시도해주세요.')
    else:
      if num<=0:
        print('음수는 지원되지 않습니다. 다시 시도해주세요.')
  for i in range(1,10):
    print(f'{num}x{i}={num*i}')
    

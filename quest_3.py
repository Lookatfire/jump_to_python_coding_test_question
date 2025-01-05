#3. 게시판 페이징 하기
"""
게시판 페이징하는 건 다음과 같다
함수 이름을 get_total_page로 설정함.
입력 데이터는 게시물의 총 개수(m), 한 페이지당 보여줄 개수(n).
출력 데이터는 총 페이지 수이다.
"""
def get_total_page(m,n):
    if m%n==0:
        return m//n
    else:
        return m//n +1

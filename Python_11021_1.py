'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.
'''

T=int(input()) # 사용자로부터 테스트 케이스의 개수 입력받기
    
for i in range(T): # i에 0부터 T-1까지 대입하며 반복
    A, B=map(int, input().split()) # 사용자로부터 두 개의 정수 입력받기
    print("Case #%d: %d" %(i+1, A+B)) # 형식에 맞춰 결과 출력하기

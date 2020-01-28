## 0. 소개
# 정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. solution 함수가 mylist 각 원소의 길이를 담은 리스트를 리턴하도록 코드를 작성해주세요.
# 제한 조건
# mylist의 길이는 100 이하인 자연수입니다.
# mylist 각 원소의 길이는 100 이하인 자연수입니다.
# 예시
# input   	                output
# [[1], [2]]	            [1,1]
# [[1, 2], [3, 4], [5]]	    [2,2,1]

# 0-1.
def solution(mylist):
    answer = []
    for a in mylist:
        answer.append(len(a))
    return answer
# 0-2.
def solution(mylist):
    return list(map(len, mylist))

## 1. 정수 다루기
# 1.1 몫과 나머지
# 문제 설명
# 숫자 a, b가 주어졌을 때 a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력해보세요.
# 입력 설명
# 입력으로는 공백으로 구분된 숫자가 두 개 주어집니다.
# 첫 번째 숫자는 a를 나타내며, 두 번째 숫자는 b를 나타냅니다.
# 출력 설명
# a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력하세요.
# 제한 조건
# a와 b는 자연수입니다.
# 입력 예
# 5 3
# 출력 예
# 1 2

# 1.1-1
a, b = map(int, input().strip().split(' '))
print(str(int(a//b)) + ' ' + str(int(a%b)))
# 1.1-2
a, b = map(int, input().strip().split(' '))
print(divmod(a,b))
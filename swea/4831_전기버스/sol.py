# K: 한 번 충전으로 최대 이동 가능한 정류장의 수
# N: 총 정류장의 개수
# M: 충전기의 개수
# charge_stops: 충전기를 설치한 정류장 번호
# 조건: 1 <= K, M, N <= 100
# 조건: 1 <= T <= 50

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    numbers = list(map(int, input().split()))
    charge_stops = list(map(int, input().split()))
    K = numbers[0]
    N = numbers[1]
    M = numbers[2]

    minimum_charge = 0
    now = 0
    now <= N




#print(f'#{tc} {minimum_charge}')
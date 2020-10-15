# 자료: 상어 위치 및 냄새 지도, 상어 이동 정보, 상어 상태 및 위치 정보, 냄새 상태 및 위치 정보
# 기능: 상어 이동 및 삭제 처리, 남은 상어 판단, 냄새 만들고 없애기
import sys

sys.stdin = open('19237_sample_input.txt', 'r')

N, M, k = map(int, input().split())

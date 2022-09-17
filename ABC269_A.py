import io
import sys

_INPUT = """\
6
1 2 5 3
10 -20 30 -40
100 100 100 -100
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  a,b,c,d=map(int,input().split())
  print((a+b)*(c-d))
  print('Takahashi')
import io
import sys

_INPUT = """\
6
11
0
576461302059761664
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  ans=[N]
  T=N
  while T>0:
    T=N&(T-1)
    ans.append(T)
  ans=sorted(ans)
  for i in range(len(ans)):
    print(ans[i])
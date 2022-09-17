import io
import sys

_INPUT = """\
6
3
1
1
1
1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  l,r=0,N
  while r-l>1:
    mid=(l+r)//2
    print('?',l+1,mid,1,N)
    T=int(input())
    if T>=mid-l: l=mid
    else: r=mid
  X=l+1
  l,r=0,N
  while r-l>1:
    mid=(l+r)//2
    print('?',1,N,l+1,mid)
    T=int(input())
    if T>=mid-l: l=mid
    else: r=mid
  Y=l+1
  print('!',X,Y)
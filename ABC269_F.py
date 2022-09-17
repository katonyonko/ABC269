import io
import sys

_INPUT = """\
6
5 4
6
1 3 2 4
1 5 1 1
5 5 1 4
4 4 2 2
5 5 4 4
1 5 1 4
1000000000 1000000000
3
1000000000 1000000000 1000000000 1000000000
165997482 306594988 719483261 992306147
1 1000000000 1 1000000000
999999999 999999999
3
999999999 999999999 999999999 999999999
216499784 840031647 84657913 415448790
1 999999999 1 999999999
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def tousa(s,d,k):
    return (2*s+(k-1)*d)*k//2%mod
  def func(i,j):
    if i==0 or j==0: return 0
    if j%2==0:
      if i%2==0:
        return (tousa(j**2//4,M*j,i//2)+tousa((2*M+2+j)*j//4,M*j,i//2))%mod
      else:
        return (tousa(j**2//4,M*j,i//2+1)+tousa((2*M+2+j)*j//4,M*j,i//2))%mod
    else:
      if i%2==0:
        return (tousa((j+1)**2//4,(j+1)*M,i//2)+tousa((j-1)*(2*M+j+1)//4,(j-1)*M,i//2))%mod
      else:
        return (tousa((j+1)**2//4,(j+1)*M,i//2+1)+tousa((j-1)*(2*M+j+1)//4,(j-1)*M,i//2))%mod

  mod=998244353
  N,M=map(int,input().split())
  Q=int(input())
  for _ in range(Q):
    A,B,C,D=map(int,input().split())
    print((func(B,D)-func(B,C-1)-func(A-1,D)+func(A-1,C-1))%mod)
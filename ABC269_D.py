import io
import sys

_INPUT = """\
6
6
-1 -1
0 1
0 2
1 0
1 2
2 0
4
5 0
4 1
-3 -4
-2 -5
5
2 1
2 -1
1 0
3 1
1 -1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  #BFS
  from collections import deque
  def bfs(G,s):
    global used
    used[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if used[y]==-1:
          dq.append(y)
          used[y]=0

  N=int(input())
  P=[list(map(int,input().split())) for _ in range(N)]
  G=[[] for _ in range(N)]
  for i in range(N):
    x,y=P[i]
    for j in range(i+1,N):
      z,w=P[j]
      if (z,w) in [(x-1,y-1),(x-1,y),(x,y-1),(x,y+1),(x+1,y),(x+1,y+1)]:
        G[i].append(j)
        G[j].append(i)
  ans=0
  used=[-1]*N
  for i in range(N):
    if used[i]==0: continue
    bfs(G,i)
    ans+=1
  print(ans)
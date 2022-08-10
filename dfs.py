from lib2to3.pgen2.pgen import DFAState


graph = [
    [1,2],
    [0,3,4],
    [4,5],
    [1],
    [1,6],
    [2],
    [4]
]

visited = [0] * 7 #방문처리 리스트
visited[0] = 1 #시작 정점 방문처리
stack = [0] # 돌아갈 곳을 기록
def dfs(start):
    stack=[start]
    visited[start]=1
    
    while len(stack) != 0: #스택이 빌 때까지 반복.
        cur = stack.pop() #현재 방문 정점(후입선출)
        
        for adj in graph[cur]: #인접한 모든 정점애 대해
            if not visited[adj]:#아직방문하지 않은 경우
                visited[adj] = 1 #방문처리
                stack.append(adj) #스택에 넣기
dfs(0)
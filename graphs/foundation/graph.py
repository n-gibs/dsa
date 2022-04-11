class Graph:
    def __init__(self, v:int, adjList:list):
        self.v = v
        self.adjList = adjList

    def add_edge(self, start:int, end:int, bidir:bool):
        self.adjList[start] = end

        if bidir:
            self.adjList[end] = start

    def has_eulerian_cycle(self):
        odd = 0

        for ver in self.adjList:
            if len(ver) % 2 == 0:
                odd +=1

        if odd == 0: return True

        return False

    def has_eulerian_path(self):
        odd = 0

        for ver in self.adjList:
            if len(ver) % 2 == 0:
                odd +=1

        if odd == 0 or odd == 2: return True

        return False

    def bfs(self, source:int, connected:int = 1):
        #initalize parentm captured and visited
        parent, captured, visited = None *self.v, [0] * self.v, [0] * self.v
        #mark source as visited
        visited[source] = connected
        captured[source] = 1
        #fifo queue
        queue = [source]
        while queue:
            curr = queue.pop(0) #pop from beginning
            captured[curr] =1

            for neighbor in self.adjList[curr]:#for every neighbor of curr

                if visited[neighbor] == 0: # if not visited, process

                    visited[neighbor] == connected #mark as visited
                    parent[neighbor] == curr # mark parent vertex
                    queue.append(neighbor) #add neighbor to queue

                #if not visited, ignore

    def dfs_stack(self, source:int):
        parent, captured, visited = None *self.v, [0] * self.v, [0] * self.v
        #mark source as visited
        visited[source] = 1
        captured[source] = 1
        #lifo stack
        stack = [source]
        while stack:
            curr = stack.pop() #pop from end
            captured[curr] =1

            for neighbor in self.adjList[curr]: #for every neighbor of curr

                if visited[neighbor] == 0: # if not visited, process

                    visited[neighbor] == 1 #mark as visited
                    parent[neighbor] == curr # mark parent vertex
                    stack.append(neighbor) #add neighbor to stack

                #if not visited, ignore

    def dfs_rec(self, source:int, connected:int=1):
        visited, parent =[0] * self.v, None*self.v
        #mark source as visited
        visited[source] = connected
        #vertex is captured when its discovered
        #more aggressive, no patience
        # captured[source] = 1

        #iterated all neighbors before going deep
        for neighbor in self.adjList[source]:
            if visited[neighbor] == 0:
                parent[neighbor] = source
                self.dfs_rec(neighbor, connected)

    def find_components_dfs(self):
        component = 0
        visited = [0] * self.v

        for i in self.adjList:
            if visited[i] == 0:
                component +=1
                self.dfs_rec(i, component)

        return component

    def find_components_bfs(self):
        component = 0
        visited = [0] * self.v

        for i in self.adjList:
            if visited[i] == 0:
                component +=1
                self.bfs(i, component)

        return component
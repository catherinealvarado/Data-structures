from collections import deque

#Topological sort:
dic = {'A':['C'],'B':['C','D'],'C':['E'],'E':['H','F'],'H':[],'F':['G'],
       'D':['F'],'G':[]}
def topological_sort(graph_dict):
    #returns a valid topological sort of directed acyclic graph above
    def helper(graph,vertex,vis,st):
        #goes through each node and updates visited and stack
        vis.add(vertex)
        for child in graph[vertex]:
            if child in vis:
                continue
            else:
                helper(graph,child,vis,st)
        st.append(vertex)

    visited = set()
    stack = deque()
    for node in graph_dict:
        if node in visited:
            continue
        else:
            helper(graph_dict,node,visited,stack)
    top_sort = []
    while stack:
        top_sort.append(stack.pop())
    return top_sort

print(topological_sort(dic))

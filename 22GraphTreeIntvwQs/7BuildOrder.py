# build order

# projects a,b,c,d,e,f
# dependencies: (a,d), (f,b), (b,d), (f,a), (d,c)

# step1 create graph
def createGraph(projects, dependencies):
    projectGraph = {}
    for project in projects:
        projectGraph[project] = []
    for pairs in dependencies:
        projectGraph[pairs[0]].extend(pairs[1])
    return projectGraph

projects = ['a','b','c','d','e','f']
dependencies = [('a','d'), ('f','b'), ('b','d'), ('f','a'), ('d','c')]

custGraph = createGraph(projects,dependencies)
print(custGraph)

# Step2 method to fing dependent nodes
def getProjectsWithDependencies(graph):
    projectsWithDependencies = set()
    for project in graph:
        projectsWithDependencies = projectsWithDependencies.union(set(graph[project]))
    return projectsWithDependencies

projectsWithDependencies = getProjectsWithDependencies(custGraph)
print(projectsWithDependencies)

# step3 find the nodes without dependencies
def getProjectsWODpendencies(projectsWD, graph):
    projectsWODependencies = set()
    for project in graph:
        if not project in projectsWD:
            projectsWODependencies.add(project)
    return projectsWODependencies

print(getProjectsWODpendencies(projectsWithDependencies, custGraph))

# Step4 take out projects wo dependencies this will make the dependendent projects independent
def findBuildOrder(projects, dependencies):
    buildOrder = []
    projectGraph = createGraph(projects, dependencies)
    while projectGraph:
        projectsWithDependencies = getProjectsWithDependencies(projectGraph)
        projectsWODependencies = getProjectsWODpendencies(projectsWithDependencies, projectGraph)
        if len(projectsWODependencies) == 0:
            raise ValueError("There is a cycle in the build order")
        for independentProjects in projectsWODependencies:
            buildOrder.append(independentProjects)
            del projectGraph[independentProjects]                   # the values of this key becomes independent

    return buildOrder


print(findBuildOrder(projects,dependencies))








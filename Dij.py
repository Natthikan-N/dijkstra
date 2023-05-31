import csv
import unittest
from test_file import DijTestCase
# print("COOL! i know u can do it!!")


class Queue:
    def __init__(self):
        self.items =[]

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self , node, priority):
        self.items.append({"node" : node , "pri":priority})
        self.items.sort(key = lambda x: x["pri"])
        # print(self.items)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def size(self):
        return len(self.items)

class Distance:
    def __init__(self , graph , start, end):
        self.graph = graph
        self.start = start.upper()
        self.end = end.upper()
        

    def display_result(self):
        # print(path)
        if self.path[len(self.path)-1].get('dis') == 0 and len(self.path) <=1 :
            print(f'no path from {self.start} to {self.end}')
            return

        print(f"Path from {self.start} to {self.end} is " , end='')
        for index ,point, in enumerate(self.path):
            if index != len(self.path)-1:
                # print(index , point)
                print( point['node'] ,end='->' )
            else:
                print(point['node'],end=', ')
        print(f'and have cost {self.path[len(self.path)-1].get("dis")}\n')
        

    def dijkstra(self):
        node = Queue()
        distance = {}
        previous = {}
        path = []

        if self.start == self.end:
            print("start node is as same as end node , please submit different end node")
            return

        # add queue 
        for vertex in self.graph:
            if vertex == self.start:
                distance[vertex] = 0
                node.enqueue(vertex, 0)
            else:
                distance[vertex] = float('inf')
                node.enqueue(vertex, float('inf'))
            previous[vertex] = None


        while node.size():
            smallest = node.dequeue()['node']
            if smallest == self.end:
                while previous[smallest]:
                    path.append({"node":smallest ,"dis" : distance[smallest]})
                    smallest = previous[smallest]
                break
            if smallest or distance[smallest] != float('inf'):
                for neighbor in self.graph[smallest] :
                    nextnode = neighbor
                    candidate = distance[smallest]+nextnode["dis"]
                    nextNeighbor = nextnode["node"]
                    if candidate < distance[nextNeighbor]:
                        distance[nextNeighbor] = candidate
                        previous[nextNeighbor] = smallest
                        node.enqueue(nextNeighbor, candidate)

        path.extend([{'node': smallest, 'dis': 0}])
        path.reverse()
        self.path = path
        self.display_result()
        return path
      
def readfile(file_name):
    datas =[]
    with open(file_name, 'r') as file:
        
        csv_reader = csv.reader(file)

        for row in csv_reader:
            column1 = row[0]
            column2 = row[1]
            column3 = row[2]
            datas.append((column1,column2,column3))
    return datas

def makegraph(datas):
    graph={}
    for data in datas:
        if data[0] not in graph:
            graph[data[0]] = []
        if data[1] not in graph:
            graph[data[1]] = []

        graph[data[0]].append({'node':data[1] , 'dis':int(data[2])})
        graph[data[1]].append({'node':data[0], 'dis':int(data[2])})
    return graph
    
def main():
    #get input from user 
    continuous = ""
    file_name = input('What is the graph file name? :')

    # read file
    datas = readfile(file_name)

    # make graph
    graph = makegraph(datas)
    
    # find path and distance
    while(continuous.lower() != 'n'):
        start_node = input('What is start node? :')
        end_node = input("What is end node? :")
        
        distance = Distance(graph, start_node, end_node)
        distance.dijkstra()
        continuous = input("Do you want to continuous(y/n)?:")

    print("Thank you ^_/\_^")

def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(DijTestCase)
    gotest = unittest.TextTestRunner()
    gotest.run(suite)

if __name__ == "__main__":
    test()
    main()
    
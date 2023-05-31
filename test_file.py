import unittest

class DijTestCase(unittest.TestCase):

    def setUp(self):
        self.datas = [
            ("A","B",2),
            ("A","D",4),
            ("B","C",3),
            ("B","D",1),
            ("C","D",1)
        ]
        
    # test making graph 
    def test_making_graph(self):
        from dij import makegraph
        result=makegraph(self.datas)
        expected_result ={
            "A":[{'node':"B" ,'dis':2}, {'node':"D" ,'dis':4}],
            "B":[{'node':"A" ,'dis':2},{'node':"C" ,'dis':3},{'node':"D" ,'dis':1}],
            "C":[{'node':"B" ,'dis':3},{'node':"D" ,'dis':1}  ],
            "D":[{'node':"A" ,'dis':4},{'node':"B" ,'dis':1},{'node':"C",'dis':1}]
         }
        self.assertEqual(expected_result, result)

    def test_AtoB(self):
        from dij import makegraph,Distance
        graph = makegraph(self.datas)
        start_node = "A"
        end_node = "B"
        expected_result = [{'node': 'A', 'dis': 0}, {'node': 'B', 'dis': 2}]
        distance = Distance(graph,start_node, end_node)
        result = distance.dijkstra()
        self.assertEqual(expected_result, result)

    def test_CtoA(self):
        from dij import makegraph ,Distance
        graph = makegraph(self.datas)
        start_node = "C"
        end_node = "A"
        expected_result = [{'node': 'C', 'dis': 0}, {'node': 'D', 'dis': 1},{'node': 'B', 'dis':2},{'node': 'A', 'dis': 4}]
        distance = Distance(graph,start_node, end_node)
        result = distance.dijkstra()
        self.assertEqual(expected_result, result)

        
if __name__ == '__main__':
    unittest.main()
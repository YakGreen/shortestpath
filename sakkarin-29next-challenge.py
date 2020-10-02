import csv
import os.path
import unittest
from sys import argv
class Graph(object):
    graph = {}
    def __init__(self):
        source_file = open("graph.csv")
        reader = csv.reader(source_file)
        for row in reader:
            if not self.graph.get(row[0]):
                self.graph[row[0]] = {}
            self.graph[row[0]][row[1]] = int(row[2])

            if not self.graph.get(row[1]):
                self.graph[row[1]] = {}
            self.graph[row[1]][row[0]] = int(row[2])
        source_file.close()

    def shortest_path(self,start, goal):
        shortest_dis = {}  # บันทึกต้นทุนเพื่อเข้าถึงโหนดนั้น จะได้รับการอัปเดตเมื่อเราเลื่อนไปตามกราฟ
        track_predecessor = {}  # ติดตามเส้นทางที่นำเราไปสู่โหนดนี้
        unseenNodes = self.graph  # เพื่อวนซ้ำทั้งกราฟ
        infinity = 999999  # infinity ca basically be considered a very Large number
        track_path = []  # จะติดตามการเดินทางของเรากลับไปยังเส้นทางที่เหมาะสมที่สุดของโหนดต้นทาง

        for node in unseenNodes:
            shortest_dis[node] = infinity
        shortest_dis[start] = 0

        while unseenNodes:
            min_dis_Node = None

            for node in unseenNodes:
                if min_dis_Node is None:
                    min_dis_Node = node
                elif shortest_dis[node] < shortest_dis[min_dis_Node]:
                    min_dis_Node = node

            path_option = self.graph[min_dis_Node].items()

            for childNode, weight in path_option:
                if weight + shortest_dis[min_dis_Node] < shortest_dis[childNode]:
                    shortest_dis[childNode] = weight + shortest_dis[min_dis_Node]
                    track_predecessor[childNode] = min_dis_Node

            unseenNodes.pop(min_dis_Node)

        currentNode = goal
        while currentNode != start:
            try:
                track_path.insert(0, currentNode)
                currentNode = track_predecessor[currentNode]
            except KeyError:
                print("Path not reachable")
                break
        track_path.insert(0, start)

        if shortest_dis[goal] != infinity:
            track_path_join = "->"
            track_path_join = track_path_join.join(track_path)
            return 'Path from ' + start + ' to ' + goal + ' is ' + str(track_path_join) + ', and have cost ' + str(shortest_dis[goal]) + '.'





class TestShoretest(unittest.TestCase):

    def test_shortest_path_with_start_A_end_B(self):
        actual = Graph().shortest_path(start="A",goal="B")
        expected = 'Path from A to B is A->B, and have cost 5.'
        self.assertEqual(actual, expected)

    def test_shortest_path_with_start_B_end_A(self):
        actual = Graph().shortest_path(start="B",goal="A")
        expected = 'Path from B to A is B->A, and have cost 5.'
        self.assertEqual(actual, expected)


    def test_shortest_path_with_start_C_end_F(self):
        actual = Graph().shortest_path(start="C",goal="F")
        expected = 'Path from C to F is C->G->H->F, and have cost 10.'
        self.assertEqual(actual, expected)


    def test_shortest_path_with_start_F_end_G(self):
        actual = Graph().shortest_path(start="F",goal="G")
        expected = 'Path from F to G is F->H->G, and have cost 8.'
        self.assertEqual(actual, expected)

    def test_shortest_path_with_start_F_end_C(self):
        actual = Graph().shortest_path(start="F",goal="C")
        expected = 'Path from F to C is F->H->G->C, and have cost 10.'
        self.assertEqual(actual, expected)


if __name__ == "__main__" :
    # while True:
    #     # print("What is graph file name: graph.csv")
    #     file = input("What is graph file name:")
    #     start = input("What is start node: ").upper()
    #     goal = input("What is goal node: ").upper()
    #     if start.isalpha() and goal.isalpha() and os.path.basename(file):
    #         break
    #     print("Please enter characters A-Z only")
    # print(Graph().shortest_path(start, goal))
    unittest.main()




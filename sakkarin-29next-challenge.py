import csv, os.path, unittest


class TestGraph(object):
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

    def shortest_path(self, start, goal):
        shortest_dis = {}
        track_history_visit = {}
        unseenNodes = self.graph
        infinity = 999999
        track_path = []

        for node in unseenNodes:
            shortest_dis[node] = infinity
        shortest_dis[start] = 0

        while unseenNodes:
            min_dis_node = None

            for node in unseenNodes:
                if min_dis_node is None:
                    min_dis_node = node
                elif shortest_dis[node] < shortest_dis[min_dis_node]:
                    min_dis_node = node

            path_option = self.graph[min_dis_node].items()

            for childNode, weight in path_option:
                if weight + shortest_dis[min_dis_node] < shortest_dis[childNode]:
                    shortest_dis[childNode] = weight + shortest_dis[min_dis_node]
                    track_history_visit[childNode] = min_dis_node

            unseenNodes.pop(min_dis_node)

        currentNode = goal
        while currentNode != start:
            try:
                track_path.insert(0, currentNode)
                currentNode = track_history_visit[currentNode]
            except KeyError:
                print("Path not reachable")
                break
        track_path.insert(0, start)

        if shortest_dis[goal] != infinity:
            track_path_join = "->"
            track_path_join = track_path_join.join(track_path)
            return 'Path from ' + start + ' to ' + goal + ' is ' + str(track_path_join) + ', and have cost ' + str(
                shortest_dis[goal]) + '.'


class TestShoretest(unittest.TestCase):

    def test_shortest_path_with_start_A_end_B(self):
        actual = TestGraph().shortest_path(start="A", goal="B")
        expected = 'Path from A to B is A->B, and have cost 5.'
        self.assertEqual(actual, expected)

    def test_shortest_path_with_start_B_end_A(self):
        actual = TestGraph().shortest_path(start="B", goal="A")
        expected = 'Path from B to A is B->A, and have cost 5.'
        self.assertEqual(actual, expected)

    def test_shortest_path_with_start_C_end_F(self):
        actual = TestGraph().shortest_path(start="C", goal="F")
        expected = 'Path from C to F is C->G->H->F, and have cost 10.'
        self.assertEqual(actual, expected)

    def test_shortest_path_with_start_F_end_G(self):
        actual = TestGraph().shortest_path(start="F", goal="G")
        expected = 'Path from F to G is F->H->G, and have cost 8.'
        self.assertEqual(actual, expected)

    def test_shortest_path_with_start_F_end_C(self):
        actual = TestGraph().shortest_path(start="F", goal="C")
        expected = 'Path from F to C is F->H->G->C, and have cost 10.'
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
# while True:
#     file = input("What is graph file name:")
#     start = input("What is start node: ").upper()
#     goal = input("What is goal node: ").upper()
#     if start.isalpha() and goal.isalpha() and os.path.basename(file):
#         break
#         print("Please enter characters A-Z only")

# if __name__ == '__main__':
#     print(TestGraph().shortest_path(start, goal))

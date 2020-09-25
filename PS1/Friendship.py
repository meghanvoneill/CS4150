class Friendship(object):

    def __init__(self, first, second):
        self.first = first
        self.second = second


class Friend(object):

    def __init__(self, name, new_friend, friend_count=0):
        self.name = name
        self.friend_count += 1

class Friendship_Graph:

    def __init__(self, friend_graph=None):
        if friend_graph is None:
            friend_graph = {}
        self.friend_graph = friend_graph

    def friends(self):
        return self.friend_graph.keys()

    def edges(self):
        return self.find_edges()

    def find_edges(self):
        edge_name = []
        for node in self.friend_graph:
            for next_node in self.friend_graph[node]:
                if {next_node, node} not in edge_name:
                    edge_name.append({})



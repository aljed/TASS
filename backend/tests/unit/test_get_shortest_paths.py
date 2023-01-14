import networkx as nx

import server

def test_get_shortest_paths() -> None:
    G: nx.DiGraph = nx.DiGraph()
    G.add_nodes_from(["A", "B", "C"])
    G.add_edge("A", "B", weight=100.)
    G.add_edge("B", "C", weight=200.)
    G.add_edge("A", "C", weight=350.)
    
    shortest_paths: list[list[str]] = server.get_shortest_paths(G, "A", "C", 2)

    assert len(shortest_paths) == 2
    assert shortest_paths[0] == ["A", "B", "C"]
    assert shortest_paths[1] == ["A", "C"]
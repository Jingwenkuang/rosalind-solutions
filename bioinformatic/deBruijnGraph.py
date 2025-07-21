import gvmagic
gvmagic.load_ipython_extension(ipython)

def de_bruijn_ize(st, k):
    edges = []
    nodes = set()

    for i in range(len(st) - k + 1):
        edges.append((st[i: i+k-1], st[i+1: i+k])) #[('AC', 'CG')]
        nodes.add(st[i: i+k-1])
        nodes.add(st[i+1: i+k])
    return nodes, edges

nodes, edges = de_bruijn_ize('ACGCGTCG', 3)
print('nodes', nodes)
print('edges', edges)

def visualize_de_bruijn(st, k):
    """ Visualize a directed multigraph using graphviz """
    nodes, edges = de_bruijn_ize(st, k)
    dot_str = 'digraph "DeBruijn graph" {\n'
    for node in nodes:
        dot_str += '  %s [label="%s"] ;\n' % (node, node)
    for src, dst in edges:
        dot_str += '  %s -> %s ;\n' % (src, dst)
    return dot_str + '}\n'

%load_ext gvmagic
%dotstr visualize_de_bruijn("ACGCGTCG", 3)
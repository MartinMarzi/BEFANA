import matplotlib
import networkx as nx


def truncate(s, n, suffix='...'):
    return s[:n] + suffix if len(s) > n+len(suffix) else s


def get_colors(n, colormap='coolwarm'):
    cm = matplotlib.cm.get_cmap(colormap)
    return [matplotlib.colors.to_hex(cm(1.0*i/n)) for i in range(n)]


def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))


def draw_network(G, axes):
    import textwrap
    pos = nx.kamada_kawai_layout(G.to_undirected())
    # pos = nx.spring_layout(G.to_undirected(), k=10, iterations=1000, seed=123)
    if G.is_directed():
        nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color="darkred", arrows=True, arrowsize=25, connectionstyle='arc3,rad=0.1', ax=axes)
    else:
        nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color="darkred", arrows=False, connectionstyle='arc3,rad=0.1', ax=axes)
    nx.draw_networkx_nodes(G, pos, alpha=0.5, node_size=500, ax=axes)
    nx.draw_networkx_labels(G, pos, alpha=0.9, font_size=12, clip_on=False, 
                            labels={node: '\n'.join(textwrap.wrap(node, 20, break_long_words=True)) for node in G.nodes},
                            horizontalalignment='left',
                            verticalalignment='top',
                            ax=axes)    
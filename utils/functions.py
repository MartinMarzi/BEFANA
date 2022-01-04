import matplotlib


def get_colors(n, colormap='coolwarm'):
    cm = matplotlib.cm.get_cmap(colormap)
    return [matplotlib.colors.to_hex(cm(1.0*i/n)) for i in range(n)]


def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))




from src.DiGraphGenerator import text_to_dict
from test import test_digraph

def main():
    filename = "data/sample2.txt"     # not necessary to add upper directory symbol(..) at the beginning of file
    dict_graph = text_to_dict(filename)
    test_digraph(dict_graph)

if __name__ == '__main__':
    main()
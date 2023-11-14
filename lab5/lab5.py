import random
import string
from graphviz import Digraph
import matplotlib.pyplot as plt
import networkx as nx


def generate_random_words():
    word_count = random.randint(20, 30)
    words = []
    for _ in range(word_count):
        word_length = random.randint(3, 10)
        word = ''.join(random.choice(string.ascii_lowercase) for _ in range(word_length))
        words.append(word)
    return ' '.join(words)


def dictionary_tree(dictionary_output, filename="dictionary_tree"):
    dot = Digraph(comment='LZ78 Dictionary Tree')
    dot.format = 'png'

    for code, phrase in dictionary_output:
        dot.node(str(code), phrase)

    for i in range(len(dictionary_output) - 1):
        dot.edge(str(dictionary_output[i][0]), str(dictionary_output[i + 1][0]), label=dictionary_output[i + 1][1][-1])

    dot.render(filename, cleanup=True, format='png', engine='dot')
    print(f"Dictionary tree saved as '{filename}.png'")


# def build_tree(dictionary_output):
#     G = nx.DiGraph()
#
#     for code, phrase in dictionary_output:
#         G.add_node(code, label=phrase)
#
#     for i in range(len(dictionary_output) - 1):
#         G.add_edge(dictionary_output[i][0], dictionary_output[i + 1][0], label=dictionary_output[i + 1][1][-1])
#
#     return G
#
#
# def draw_dictionary_tree(graph, filename="dictionary_tree"):
#     pos = nx.spring_layout(graph)
#     labels = nx.get_edge_attributes(graph, 'label')
#     nx.draw(graph, pos, with_labels=True, labels=nx.get_node_attributes(graph, 'label'), node_size=700, node_color='skyblue', font_size=8, font_color='black')
#     nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_color='red', font_size=8)
#
#     plt.savefig(f"{filename}.png")
#     plt.show()


def build_tree(dictionary_output):
    dot = Digraph(comment='LZ78 Dictionary Tree')

    for code, phrase in dictionary_output:
        dot.node(str(code), phrase)

    for i in range(len(dictionary_output) - 1):
        edge_label = dictionary_output[i + 1][1][-1]
        dot.edge(str(dictionary_output[i][0]), str(dictionary_output[i + 1][0]), label=edge_label, fontsize='8')

    return dot


def draw_dictionary_tree(dot, filename="dictionary_tree"):
    dot.render(filename, cleanup=True, format='png', engine='dot')
    print(f"Dictionary tree saved as '{filename}.png'")


class LZ78:
    def __init__(self):
        self.dictionary = {0: ''}
        self.next_code = 1

    def compress(self, data):
        compressed_data = []
        current_phrase = ''
        dictionary_output = []

        for symbol in data:
            if current_phrase + symbol in self.dictionary:
                current_phrase += symbol
            else:
                code = self.dictionary.get(current_phrase, 0)
                compressed_data.append((code, symbol))
                dictionary_output.append((code, current_phrase + symbol))
                self.dictionary[current_phrase + symbol] = self.next_code
                self.next_code += 1
                current_phrase = ''

        if current_phrase:
            code = self.dictionary.get(current_phrase, 0)
            compressed_data.append((code, ''))
            dictionary_output.append((code, current_phrase))

        return compressed_data, dictionary_output

    def decompress(self, compressed_data):
        self.dictionary = {0: ''}
        self.next_code = 1
        data = ''
        dictionary_output = []

        for code, symbol in compressed_data:
            if code in self.dictionary:
                phrase = self.dictionary[code]
            else:
                phrase = self.dictionary[code - 1] + self.dictionary[code - 1][0]
            phrase += symbol
            data += phrase
            dictionary_output.append((self.next_code, phrase))
            self.dictionary[self.next_code] = phrase
            self.next_code += 1

        return data, dictionary_output

    def get_average_code_length(self, compressed_data):
        total_length = 0
        total_count = 0

        for code, next_symbol in compressed_data:
            total_length += len(bin(code)[2:])
            total_count += 1

        return total_length / total_count if total_count > 0 else 0


def print_table(dict, comp):
    for i in dict:
        print(i[1])

    print('\n\n -----------------------------\n\n')

    for i in comp:
        print(i)


if __name__ == "__main__":
    sequence_1 = "sir_sid_eastman_easily_teases_sea_sick_seals"
    # sequence_1 = "moskalmoskal"
    sequence_2 = ("Get clear definitions and audio pronunciations of words, phrases, and idioms in British and American"
                  "English from the three most popular Cambridge dictionaries of English with just one search")
    sequence_3 = generate_random_words()

    lz1 = LZ78()
    lz2 = LZ78()
    lz3 = LZ78()

    compressed_data_1, dictionary_compress_1 = lz1.compress(sequence_1)
    compressed_data_2, dictionary_compress_2 = lz2.compress(sequence_2)
    compressed_data_3, dictionary_compress_3 = lz3.compress(sequence_3)

    print("Compressed data 1:", compressed_data_1)
    print("Compressed data 2:", compressed_data_2)
    print("Compressed data 3:", compressed_data_3)
    print("Dictionary (during compression) 1:", dictionary_compress_1)
    print("Dictionary (during compression) 2:", dictionary_compress_2)
    print("Dictionary (during compression) 3:", dictionary_compress_3)

    average_length_1 = lz1.get_average_code_length(compressed_data_1)
    average_length_2 = lz2.get_average_code_length(compressed_data_2)
    average_length_3 = lz3.get_average_code_length(compressed_data_3)
    decompressed_data_1, dictionary_decompress_1 = lz1.decompress(compressed_data_1)
    decompressed_data_2, dictionary_decompress_2 = lz2.decompress(compressed_data_2)
    decompressed_data_3, dictionary_decompress_3 = lz3.decompress(compressed_data_3)

    print("Average length 1:", average_length_1)
    print("Average length 2:", average_length_2)
    print("Average length 3:", average_length_3)
    print("Decompressed data 1:", decompressed_data_1)
    print("Decompressed data 2:", decompressed_data_2)
    print("Decompressed data 3:", decompressed_data_3)
    print("Dictionary (during decompression) 1:", dictionary_decompress_1)
    print("Dictionary (during decompression) 2:", dictionary_decompress_2)
    print("Dictionary (during decompression) 3:", dictionary_decompress_3)

    # dictionary_tree(dictionary_compress_1, "dict_tree_1")
    # draw_dictionary_tree(dictionary_compress_2, "dictionary_tree_2")
    draw_dictionary_tree(build_tree(dictionary_compress_1), "dictionary_tree_1")
    draw_dictionary_tree(build_tree(dictionary_compress_2), "dictionary_tree_2")

    print_table(dictionary_compress_1, compressed_data_1)


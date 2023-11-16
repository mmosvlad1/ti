import random
import string
from math import ceil

import graphviz
from treelib import Tree


def generate_random_words():
    word_count = random.randint(20, 30)
    words = []
    for _ in range(word_count):
        word_length = random.randint(3, 10)
        word = ''.join(random.choice(string.ascii_lowercase) for _ in range(word_length))
        words.append(word)
    return '_'.join(words)


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

        return ceil(total_length / total_count) if total_count > 0 else 0


def show_tree(compressed, name):
    tree = Tree()
    tree.create_node("Root", "0")

    for i in range(len(compressed)):
        symbol = compressed[i][1]
        parent_index = str(compressed[i][0])
        tree.create_node(f"{symbol} ({i})", f"{i + 1}", parent=parent_index)

    tree.show()

    dot = graphviz.Digraph(comment='Tree Visualization')

    for node in tree.all_nodes():
        if node.identifier != '0':
            parent_node = tree.parent(node.identifier)
            dot.node(node.identifier, node.tag)
            dot.edge(parent_node.identifier, node.identifier)

    dot.attr(rankdir='LR')
    dot.attr(ratio='fill')

    dot.render(f"tree_visualization{name}", view=True)


if __name__ == "__main__":
    sequence_1 = "moskalmoskal"
    sequence_2 = ("Get_clear_definitions_and_audio_pronunciations_of_words_phrases_and_idioms_in_British_and_American"
                  "_English_from_the_three_most_popular_Cambridge_dictionaries_of_English_with_just_one_search")
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

    show_tree(dictionary_compress_1, '1')
    show_tree(dictionary_compress_2, '2')

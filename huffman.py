import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(data):
    return Counter(data)

def build_huffman_tree(freq_table):
    heap = [HuffmanNode(freq, char) for char, freq in freq_table.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged_node = HuffmanNode(node1.freq + node2.freq)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(heap, merged_node)

    return heapq.heappop(heap)

def build_codeword_table(tree):
    codeword_table = {}

    def traverse(node, codeword):
        if node.char:
            codeword_table[node.char] = codeword
            return

        traverse(node.left, codeword + '0')
        traverse(node.right, codeword + '1')

    traverse(tree, '')
    return codeword_table

def huffman_encode(data):
    if not data:
        return None, None

    freq_table = build_frequency_table(data)
    huffman_tree = build_huffman_tree(freq_table)
    codeword_table = build_codeword_table(huffman_tree)

    encoded_data = ''.join(codeword_table[char] for char in data)
    return encoded_data, huffman_tree

def huffman_decode(encoded_data, huffman_tree):
    if not encoded_data or not huffman_tree:
        return None

    decoded_data = []
    current_node = huffman_tree

    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char:
            decoded_data.append(current_node.char)
            current_node = huffman_tree

    return ''.join(decoded_data)

# Example usage
if __name__ == "__main__":
    data = "abracadabra"
    print("Original data:", data)

    encoded_data, huffman_tree = huffman_encode(data)
    print("Encoded data:", encoded_data)

    decoded_data = huffman_decode(encoded_data, huffman_tree)
    print("Decoded data:", decoded_data)

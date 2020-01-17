class TrieTree:
    class Node:
        def __init__(self, char='*'):
            self.char = char
            self.children = []
            self.is_word = False

    def __init__(self):
        self.root = self.Node()

    def add(self, word):
        node = self.root

        for char in word:
            found = False
            for child in node.children:
                if child.char == char:
                    node = child
                    found = True
                    break

            if not found:
                new_node = self.Node(char)
                node.children.append(new_node)
                node = new_node

        node.is_word = True

    def find(self, pattern):
        node = self.root

        for char in pattern:
            for child in node.children:
                if child.char == char:
                    node = child
                else:
                    return False
        return True


trie = TrieTree()
trie.add('hackathon')
trie.add('hack')

print(trie.find('hac'))
print(trie.find('hack'))
print(trie.find('hammer'))
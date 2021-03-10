"""
* 트라이 구현
트라이의 insert, search, startsWith 메소드를 구현하라.
- Example
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple"); // returns true
trie.search("app"); // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app"); // returns true
"""

# 트라이를 저장할 노드 클래스
import collections


class TrieNode:
    def __init__(self):
        # 단어가 모두 완성되었을 시 True로 변경
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True

if __name__ == '__main__':
    t = Trie()
    t.insert("apple")

class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie["end"] = True
        return

    def search(self, word: str) -> bool:
        sub_tries = [self.trie.copy()]
        for char in word:
            sub_tries_tmp = []
            for sub_trie in sub_tries:
                if char == '.':
                    for key, value in sub_trie.items():
                        if key == 'end':
                            continue
                        sub_tries_tmp.append(value)
                else:
                    if char in sub_trie:
                        sub_tries_tmp.append(sub_trie[char])
            if not sub_tries_tmp:
                return False
            sub_tries = sub_tries_tmp

        for sub_trie in sub_tries:
            if sub_trie.get("end", False):
                return True
        return False

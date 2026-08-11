class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word # Mark end of a word
        
        rows, cols = len(board), len(board[0])
        found_words = set()
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c, node):
            # Boundary checks and visited check
            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c]:
                return
            
            char = board[r][c]
            if char not in node.children:
                return
            
            # Move to the next node in Trie 
            node = node.children[char]

            # If it's a word, add to results and mark as None to avoid duplicates
            if node.word:
                found_words.add(node.word)
                # Optimization : Remove the word from Trie to prune further searches
                # if we dont want to find the same word multiple times from different paths.
                # For this problem, we need to find *all* occurrences, so we dont remove  the word here,
                # but rather manage duplicates with the 'found_words' set.
                # If a word can be formed in multiple ways, we only add it once to the set.
                # A common optimization is to set node.word = None AFTER adding to result if we are 
                # sure we dont need to find this exactword again in this path.
                # If node.word is set to None, it would stop finding this word again.
                # For example, if "oath" is found, and then "oath" is a prefix for "oathful" if it continues from this node.
                # A better approach for this problem is to remove the word from the *dictionary* (or Trie branch) once found to avoid redundant checks for that specific word.
                # For simplicity with the current Trie structure, we'll use the set.
                # A common variation is 'node.word = None' to prevent re-adding it from this specific branch.
                # If we dont do this, and "oath" exists and then "oathful" exists, and we find "oath" then we would continue DFS, and if "oathful" is in the Trie path, we'd find it.

            visited[r][c] = True

            # Explore neighbors
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            # Backtrack 
            visited[r][c] = False
        # Start DFS from each cell in the board
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return list(found_words)
        
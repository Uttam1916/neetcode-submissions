from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        indegree = defaultdict(int)

        for word in words:
            for ch in word:
                indegree[ch] = 0

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            minlen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""

            for j in range(minlen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        q = deque(ch for ch in indegree if indegree[ch] == 0)
        res = []

        while q:
            node = q.popleft()
            res.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(res) != len(indegree):
            return ""

        return "".join(res)
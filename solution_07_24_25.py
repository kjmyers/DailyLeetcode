class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        # Calculate XOR of subtree rooted at each node
        subtree_xor = [0] * n
        subtree_nodes = [[] for _ in range(n)]
        
        def dfs(node: int, parent: int) -> None:
            subtree_xor[node] = nums[node]
            subtree_nodes[node].append(node)
            for neighbor in adj[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
                    subtree_xor[node] ^= subtree_xor[neighbor]
                    subtree_nodes[node].extend(subtree_nodes[neighbor])
        
        dfs(0, -1)
        
        # Total XOR of all nodes
        total_xor = subtree_xor[0]
        
        min_score = float('inf')
        
        # Try all possible pairs of edges to remove
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                # Get the two edges to remove
                edge1, edge2 = edges[i], edges[j]
                
                # For each edge, choose the node that leads to smaller subtree
                node1 = edge1[1] if len(subtree_nodes[edge1[1]]) < len(subtree_nodes[edge1[0]]) else edge1[0]
                node2 = edge2[1] if len(subtree_nodes[edge2[1]]) < len(subtree_nodes[edge2[0]]) else edge2[0]
                
                # Handle cases where one subtree is contained in another
                if node2 in subtree_nodes[node1]:
                    # node2 is in node1's subtree
                    xor1 = subtree_xor[node2]
                    xor2 = subtree_xor[node1] ^ xor1
                    xor3 = total_xor ^ subtree_xor[node1]
                elif node1 in subtree_nodes[node2]:
                    # node1 is in node2's subtree
                    xor1 = subtree_xor[node1]
                    xor2 = subtree_xor[node2] ^ xor1
                    xor3 = total_xor ^ subtree_xor[node2]
                else:
                    # Subtrees are disjoint
                    xor1 = subtree_xor[node1]
                    xor2 = subtree_xor[node2]
                    xor3 = total_xor ^ xor1 ^ xor2
                
                # Calculate score
                max_xor = max(xor1, xor2, xor3)
                min_xor = min(xor1, xor2, xor3)
                score = max_xor - min_xor
                min_score = min(min_score, score)
        
        return min_score

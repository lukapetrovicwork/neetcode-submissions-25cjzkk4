class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        l, r = 0, k
        best = 99999999

        while r <= len(blocks):
            moves = 0
            for n in range(l, r):
                if blocks[n] == "W":
                    moves = moves + 1
            if moves < best:
                best = moves
            r = r + 1
            l = l + 1
            
        return best
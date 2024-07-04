from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: 'list[list[str]]') -> bool:
        rset = defaultdict(set) # row
        cset = defaultdict(set) # col
        rcset = defaultdict(set) # row, col which is at a higher level i.e. / 3

        for r in range(len(board)):
            for c in range(len(board[0])):
                curr = board[r][c]
                if curr == ".":
                    continue
                if curr in rset[r] or curr in cset[c]:
                    return False
                rset[r].add(curr)
                cset[c].add(curr)
                high_r = r // 3
                high_c = c // 3
                if curr in rcset[(high_r, high_c)]:
                    return False
                rcset[(high_r,high_c) ].add(curr)
        return True
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        con = goal + goal
        if s in con:
            return True
        return False
                    
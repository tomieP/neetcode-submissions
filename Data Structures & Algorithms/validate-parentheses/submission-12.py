class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        h = {
            '}':'{',
            ')':'(',
            ']':'['
        }

        for c in s:
            if c in h:
                if st and st[-1] == h[c]:
                        st.pop()
                else: return False
            else:
                st.append(c)
        return True if not st else False
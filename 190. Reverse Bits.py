class Solution:
    def reverseBits(self, n: int) -> int:
        n_bin = str(bin(n)[2:])
        pre = ''.join(['0' for _ in range(32-len(n_bin))])
        n_bin = pre + n_bin
        n_bin = n_bin[::-1]
        return int(n_bin, 2)
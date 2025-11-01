class Hanoi:
    def __init__(self):
        self.moves = []

    def solve(self, n, a = "A", b = 'B', c = 'C'):
        if n == 1:
            self.moves.append((a, c))
        else:
            self.solve(n - 1 , a, c, b)
            self.moves.append((a, c))
            self.solve(n - 1, b, a, c)

if __name__ == "__main__":
    n = 2
    h = Hanoi()
    h.solve(n, "A", "B", "C")

    total = (1 << n) - 1
    print("移動動作")
    for a, b in h.moves:
        print(f"{a} -> {b}")
    print("Done")
    print(f"總共需要 {total} 次移動")
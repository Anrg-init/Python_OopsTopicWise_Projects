class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # print(v)
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # v1 + v2
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # v1 - v2
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # v1 * 3  (scale the vector)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # v1 == v2
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # v1 > v2  (compare lengths)
    def __gt__(self, other):
        return len(self) > len(other)

    # v1 < v2
    def __lt__(self, other):
        return len(self) < len(other)

    # len(v)  (length/magnitude of vector)
    def __len__(self):
        return int((self.x**2 + self.y**2) ** 0.5)

    # repr(v)  (developer view)
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"


# ── creating vectors ──────────────────────────────
v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = Vector(3, 4)

# ── __str__ ───────────────────────────────────────
print(v1)              # Vector(3, 4)
print(v2)              # Vector(1, 2)

# ── __add__ ───────────────────────────────────────
print(v1 + v2)         # Vector(4, 6)

# ── __sub__ ───────────────────────────────────────
print(v1 - v2)         # Vector(2, 2)

# ── __mul__ ───────────────────────────────────────
print(v1 * 3)          # Vector(9, 12)

# ── __eq__ ────────────────────────────────────────
print(v1 == v3)        # True  — same x and y
print(v1 == v2)        # False — different x and y

# ── __gt__ __lt__ ─────────────────────────────────
print(v1 > v2)         # True  — v1 is longer
print(v1 < v2)         # False

# ── __len__ ───────────────────────────────────────
print(len(v1))         # 5    — √(3²+4²) = √25 = 5
print(len(v2))         # 2    — √(1²+2²) = √5  ≈ 2

# ── __repr__ ──────────────────────────────────────
print(repr(v1))        # Vector(x=3, y=4)
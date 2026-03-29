Operator Overloading

Operator overloading concept

__add__

__sub__

__eq__

Custom operator behavior


## notes
## Operator Overloading

When you define **what an operator does** for your own class. Python calls special dunder methods behind the scenes for every operator.

---

## 1. The Concept

```python
print(10 + 20)         # Python knows what + means for int
print("hi" + "bye")    # Python knows what + means for string

class Money:
    def __init__(self, amount):
        self.amount = amount

m1 = Money(100)
m2 = Money(200)
print(m1 + m2)         # ❌ TypeError — Python doesn't know what + means for Money
```

Python has no idea what `+` means for YOUR class. You have to tell it — that's operator overloading.

Every operator has a dunder method behind it:

```python
a + b     →   a.__add__(b)
a - b     →   a.__sub__(b)
a * b     →   a.__mul__(b)
a == b    →   a.__eq__(b)
a > b     →   a.__gt__(b)
print(a)  →   a.__str__()
len(a)    →   a.__len__()
```

Python automatically calls these when you use the operator.

---

## 2. `__add__` — The + Operator

```python
class Money:
    def __init__(self, amount, currency="INR"):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        return Money(self.amount + other.amount, self.currency)

    def __str__(self):
        return f"{self.currency} {self.amount}"

m1 = Money(100)
m2 = Money(200)

m3 = m1 + m2           # Python calls m1.__add__(m2) automatically
print(m3)              # INR 300
```

Step by step what happens:
```python
m1 + m2
# Python sees +
# calls m1.__add__(m2)
# self = m1, other = m2
# returns Money(100 + 200) = Money(300)
```

---

## 3. `__sub__` — The - Operator

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __sub__(self, other):
        if other.amount > self.amount:
            raise ValueError("not enough balance")
        return Money(self.amount - other.amount)

    def __str__(self):
        return f"INR {self.amount}"

m1 = Money(500)
m2 = Money(200)

m3 = m1 - m2           # calls m1.__sub__(m2)
print(m3)              # INR 300

m4 = m2 - m1           # 200 - 500
# ValueError: not enough balance
```

---

## 4. `__eq__` — The == Operator

Without `__eq__`, Python compares **memory addresses**, not values:

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

m1 = Money(100)
m2 = Money(100)

print(m1 == m2)    # ❌ False — different objects in memory, even though same amount
```

With `__eq__`:

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount    # now compares values

m1 = Money(100)
m2 = Money(100)
m3 = Money(200)

print(m1 == m2)    # ✅ True  — same amount
print(m1 == m3)    # ✅ False — different amount
```

---

## 5. All Together — Custom `Money` Class

```python
class Money:
    def __init__(self, amount, currency="INR"):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):                        # m1 + m2
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):                        # m1 - m2
        if other.amount > self.amount:
            raise ValueError("not enough balance")
        return Money(self.amount - other.amount, self.currency)

    def __eq__(self, other):                         # m1 == m2
        return self.amount == other.amount

    def __gt__(self, other):                         # m1 > m2
        return self.amount > other.amount

    def __lt__(self, other):                         # m1 < m2
        return self.amount < other.amount

    def __str__(self):                               # print(m1)
        return f"{self.currency} {self.amount}"


m1 = Money(500)
m2 = Money(200)
m3 = Money(500)

print(m1 + m2)     # INR 700
print(m1 - m2)     # INR 300
print(m1 == m3)    # True
print(m1 == m2)    # False
print(m1 > m2)     # True
print(m2 < m1)     # True
print(m1)          # INR 500
```

---

## Complete Dunder Reference

| Operator | Dunder | Example |
|---|---|---|
| `+` | `__add__` | `m1 + m2` |
| `-` | `__sub__` | `m1 - m2` |
| `*` | `__mul__` | `m1 * 2` |
| `/` | `__truediv__` | `m1 / 2` |
| `==` | `__eq__` | `m1 == m2` |
| `!=` | `__ne__` | `m1 != m2` |
| `>` | `__gt__` | `m1 > m2` |
| `<` | `__lt__` | `m1 < m2` |
| `>=` | `__ge__` | `m1 >= m2` |
| `<=` | `__le__` | `m1 <= m2` |
| `print()` | `__str__` | `print(m1)` |
| `len()` | `__len__` | `len(m1)` |

---

## The Big Picture

```
You write →   m1 + m2
Python sees → m1.__add__(m2)
You define  → __add__ → controls what happens
Result      → whatever you return from __add__
```

You are literally **redefining** what operators mean for your class. That's the power of operator overloading.
# =============================================
# Python Data Structures - Beginner's Guide 📚
# =============================================

# ---------------------------------------------
# 🧱 Lists - Ordered, mutable, allows duplicates
# ---------------------------------------------
my_list = [1, 2, 3, 4]
my_list.append(5)
print("First element of list:", my_list[0])
my_list[2] = 10
print("Updated list:")
for item in my_list:
    print(item)

# ---------------------------------------------
# 🔢 Tuples - Ordered, immutable, allows duplicates
# ---------------------------------------------
my_tuple = (1, 2, 3)
print("Tuple contents:", my_tuple)
print("Second element:", my_tuple[1])
# my_tuple[0] = 10  # ❌ Error: Tuples are immutable

# ---------------------------------------------
# 📌 Sets - Unordered, mutable, only unique elements
# ---------------------------------------------
my_set = {1, 2, 3}
my_set.add(4)
if 2 in my_set:
    print("2 is in the set")
print("Set contents:")
for item in my_set:
    print(item)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# ---------------------------------------------
# 📦 Dictionaries - Ordered (as of Python 3.7+), mutable, key-value pairs
# ---------------------------------------------
my_dict = {"name": "John", "age": 30}
print("Name:", my_dict["name"])
my_dict["city"] = "New York"
print("Dictionary contents:")
for key, value in my_dict.items():
    print(key, value)

# ---------------------------------------------
# 🔁 Loops
# ---------------------------------------------
print("For loop:")
for i in range(5):
    print(i)

print("While loop:")
x = 0
while x < 5:
    print(x)
    x += 1

# ---------------------------------------------
# 🧮 Function Example
# ---------------------------------------------
def add(a, b):
    return a + b

print("add(2, 3) =", add(2, 3))

# ---------------------------------------------
# 🧊 defaultdict - auto-initializes missing keys
# ---------------------------------------------
from collections import defaultdict

dd = defaultdict(list)
dd["key"].append(1)
print("Defaultdict contents:", dict(dd))  # Convert to regular dict for display

# ---------------------------------------------
# 🎯 deque - Double-ended queue for fast appends/pops on both ends
# ---------------------------------------------
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print("Deque after appendleft and append:", list(dq))
dq.popleft()
dq.pop()
print("Deque after pops:", list(dq))

# ---------------------------------------------
# 👤 namedtuple - Lightweight object with named fields
# ---------------------------------------------
from collections import namedtuple

Person = namedtuple("Person", ["name", "age"])
p = Person(name="Alice", age=28)
print("NamedTuple:", p.name, p.age)

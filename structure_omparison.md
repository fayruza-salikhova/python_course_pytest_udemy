## 🧩 Structure Comparison Summary

| Structure   | Ordered | Mutable | Unique Elements | Fast Lookup |
|-------------|:-------:|:-------:|:----------------:|:-----------:|
| List        |   ✅    |   ✅    |        ❌        |      ❌      |
| Tuple       |   ✅    |   ❌    |        ❌        |      ❌      |
| Set         |   ❌    |   ✅    |        ✅        |      ✅      |
| Dict        |   ✅    |   ✅    |    Keys: ✅      |      ✅      |
| Deque       |   ✅    |   ✅    |        ❌        | Partial ✅  |
| NamedTuple  |   ✅    |   ❌    |        ❌        |   Attribute ✅ |

---

## ⏱️ Time Complexity Summary (Big-O Notation)

| Operation           | List     | Tuple    | Set      | Dict     | Deque    |
|---------------------|----------|----------|----------|----------|----------|
| Create              | O(n)     | O(n)     | O(n)     | O(n)     | O(n)     |
| Index access        | O(1)     | O(1)     | N/A      | O(1)     | O(1)     |
| Search (in)         | O(n)     | O(n)     | O(1)     | O(1)     | O(n)     |
| Append              | O(1)*    | ❌       | O(1)     | O(1)     | O(1)     |
| Insert at front     | O(n)     | ❌       | ❌       | ❌       | O(1)     |
| Pop from end/front  | O(1)/O(n)| ❌       | ❌       | O(1)     | O(1)     |
| Delete element      | O(n)     | ❌       | O(1)     | O(1)     | O(1)     |

> \* `list.append()` is amortized O(1), but can be O(n) when resizing occurs.

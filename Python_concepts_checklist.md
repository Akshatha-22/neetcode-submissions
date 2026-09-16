# Python Concepts Checklist for NeetCode 250

Work through tiers in order — each one assumes fluency in the concepts before it.

## Tier 1 — Foundations (Arrays & Hashing)
- [ ] Lists: indexing, slicing, `append`/`pop`/`insert`, list comprehensions
- [ ] Dicts: `dict.get()`, `in` checks, `defaultdict`, `collections.Counter`
- [ ] Sets: membership testing, set operations (`&`, `|`, `-`)
- [ ] Tuples: as dict keys, unpacking (`a, b = b, a`)
- [ ] `sorted()` with `key=lambda` and `reverse=True`
- [ ] String basics: slicing, `split`/`join`, `ord`/`chr`, immutability (build with a list, then `join`)

## Tier 2 — Two Pointers / Sliding Window / Stack
- [ ] `while` loop pointer manipulation (`left`, `right` indices)
- [ ] `collections.deque`: `append`, `appendleft`, `pop`, `popleft` (O(1) both ends)
- [ ] List-as-stack (`append`/`pop` from the end)
- [ ] Truthy/falsy pitfalls (`0`, `""`, `[]`)

## Tier 3 — Binary Search
- [ ] Manual `lo`/`hi`/`mid` template, off-by-one awareness
- [ ] `bisect_left`/`bisect_right` from the `bisect` module
- [ ] `//` (floor division) vs `/` — Python has no integer overflow, but watch this

## Tier 4 — Linked List
- [ ] Classes and `self`, defining a `Node`/`ListNode`
- [ ] Reference semantics (why `curr = curr.next` doesn't copy)
- [ ] Dummy node pattern
- [ ] `None` checks and short-circuit evaluation (`a and a.next`)

## Tier 5 — Trees
- [ ] Recursion fundamentals: base case, call stack depth
- [ ] `sys.setrecursionlimit()` (occasionally needed)
- [ ] BFS with `deque` (level order)
- [ ] DFS with recursion vs explicit stack
- [ ] Returning tuples/multiple values from recursive calls

## Tier 6 — Tries / Heap / Backtracking
- [ ] Nested dicts for Trie nodes (`defaultdict(dict)` or custom class)
- [ ] `heapq`: `heappush`, `heappop`, negating values for max-heap simulation, heap of tuples
- [ ] Backtracking pattern: `path.append(x)` → recurse → `path.pop()`
- [ ] **Pitfall**: `result.append(path)` vs `result.append(path[:])` (shallow copy issue)
- [ ] `itertools`: `permutations`, `combinations`, `product`

## Tier 7 — Intervals / Greedy
- [ ] Sorting by custom key (`key=lambda x: x[0]`)
- [ ] `functools.reduce` (occasionally)
- [ ] Merging logic with in-place list mutation vs building a new list

## Tier 8 — Graphs
- [ ] Adjacency list via `defaultdict(list)`
- [ ] Visited sets vs visited arrays
- [ ] Union-Find: implementing with a dict or list (`parent[]`, `rank[]`)
- [ ] BFS/DFS on grids: encoding coordinates as `(r, c)` tuples in a set
- [ ] Cycle detection (course schedule pattern)
- [ ] Topological sort (Kahn's algorithm using deque + in-degree dict)

## Tier 9 — 1D Dynamic Programming
- [ ] Memoization via `functools.lru_cache` on recursive functions
- [ ] Bottom-up with array/dict, understanding state transitions
- [ ] Space optimization (rolling variables instead of full array)

## Tier 10 — 2D Dynamic Programming
- [ ] 2D list initialization: `[[0]*cols for _ in range(rows)]` — **not** `[[0]*cols]*rows` (shares references!)
- [ ] Iterating with nested loops, base case rows/columns
- [ ] `lru_cache` with multiple arguments

## Tier 11 — Bit Manipulation
- [ ] `&`, `|`, `^`, `~`, `<<`, `>>`
- [ ] `bin()`, counting set bits, XOR tricks
- [ ] Python's arbitrary-precision ints — no fixed-width overflow, but be careful with `~` and negative numbers

## Tier 12 — Math & Geometry
- [ ] `//`, `%`, `divmod()`
- [ ] `math` module: `sqrt`, `gcd`, `factorial`
- [ ] Matrix rotation/transpose via nested list indexing or `zip(*matrix)`
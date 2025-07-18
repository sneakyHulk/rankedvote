# RankedVote — Simple Ranked Voting with Schulze and STV
RankedVote is a lightweight and easy-to-use Python library for doing ranked-choice elections, with built-in support for:

1. Schulze method
  - Supports partial ballots and tied rankings
2. Single Transferable Vote (STV)
  - Supports partial ballots

---
## Installation

You can install directly from GitHub:

```bash
pip install git+https://github.com/sneakyHulk/rankedvote.git
```

## Example Usage

```python
from rankedvote.methods import schulze, stv
from rankedvote.output import output

votes = [
    ["E", "F", "B", "A", "D", "G", "H", "I"],
    ["A", "B", "E", "G", "H"],
    ["D", "A", "E", "F", "B", "I", "H", "G"],
    ["E", "I", "B", "A", "D", "F", "G", "H"],
    ["A", "F", "E", "B", "D", "I", "H", "G"],
    ["A", "I", "F", "B", "D", "H", "E", "G"],
    ["A", "B", "E", "D", "F", "I", "G", "H"],
    ["A", "F", "I", "B", "D", "E", "G", "H"],
    ["A", "E", "B", "D", "I", "F", "H", "G"],
    ["I", "B", "D", "E", "F", "G"],
    ["D", "G", "B", "E", "F", "A", "I", "H"],
    ["E", "A", "D", "B", "F", "H", "G"],
    ["A", "I", "F", "B", "D", "G", "H", "E"],
    ["A", "I", "D", "B", "F", "E", "G", "H"],
    ["A", "E", "D", "B", "G", "H"],
    ["D", "I", "E", "F", "A", "B", "G", "H"],
    ["A", "E", "G", "I", "F", "D", "H", "B"]
]

# Schulze Method
print("Schulze:")
rankings, positions = schulze(votes)
output((rankings, positions))

# STV Method
print("STV:")
rankings, positions = stv(votes)
output((rankings, positions))
```

#### Output

```text
Schulze:
1. ['A']
2. ['D', 'E']
4. ['I']
5. ['B', 'F', 'G', 'H']
STV:
1. ['A']
2. ['E']
3. ['B']
4. ['D']
5. ['I']
6. ['F']
7. ['G']
8. ['H']
```
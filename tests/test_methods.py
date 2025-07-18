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


def test_schulze():
    result = schulze(votes)
    print()
    output(result)
    assert schulze(votes) == ([['A'], ['D', 'E'], ['I'], ['B', 'F', 'G', 'H']], [1, 2, 4, 5])


def test_stv():
    result = stv(votes)
    print()
    output(result)
    assert stv(votes) == ([['A'], ['E'], ['B'], ['D'], ['I'], ['F'], ['G'], ['H']], [1, 2, 3, 4, 5, 6, 7, 8])
def output(result: tuple[list[list[str]], list[int]]):
    for ranking, position in zip(*result):
        print(str(position) + ".", ranking)

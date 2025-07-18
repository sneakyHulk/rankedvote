from pyrankvote import Candidate, Ballot, single_transferable_vote
from py3votecore.schulze_pr import SchulzePR
from py3votecore.condorcet import CondorcetHelper


def schulze(votes: list[list[str]]):
    unique_candidates = set().union(*votes)
    missing_candidates = [unique_candidates - set().union(vote) for vote in votes]
    votes = [[[choice] for choice in vote] + [list(missing)] if missing else [[choice] for choice in vote] for
             vote, missing
             in zip(votes, missing_candidates)]

    unique_votes = []
    counts = []
    for vote in votes:
        if vote not in unique_votes:
            unique_votes.append(vote)
            counts.append(1)
        else:
            counts[unique_votes.index(vote)] = counts[unique_votes.index(vote)] + 1

    ballots = [{'count': count, 'ballot': person} for person, count in zip(unique_votes, counts)]
    result = SchulzePR(ballots, ballot_notation=CondorcetHelper.BALLOT_NOTATION_GROUPING).as_dict()

    rankings = []
    position = []

    iterator = enumerate(result['rounds'], 1)
    for i, rank in iterator:
        if 'tied_winners' in rank:
            rankings.append([choice for choice in sorted(rank['tied_winners'])])
            position.append(i)
            for _ in range(len(rank['tied_winners']) - 1): next(iterator, None)
        else:
            rankings.append([rank['winner']])
            position.append(i)

    return rankings, position


def stv(votes: list[list[str]]):
    unique_candidates = {candidate: Candidate(candidate) for candidate in set().union(*votes)}
    votes = [[unique_candidates[choice] for choice in vote] for vote in votes]
    winners = []

    rankings = []
    position = []

    for i, _ in enumerate(unique_candidates, 1):
        candidates = set(unique_candidates.values()) - set(winners)
        ballots = [Ballot(vote) for vote in votes]
        result = single_transferable_vote(list(candidates), ballots, 1)

        rankings.append([choice.name for choice in result.get_winners()])
        position.append(i)

        winners = winners + result.get_winners()
        votes = [[choice for choice in vote if not choice in result.get_winners()] for vote in votes if
                 not vote == result.get_winners()]

    return rankings, position
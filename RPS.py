def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if not opponent_history:
        return "R"

    # Simple strategy: counter most frequent move
    from collections import Counter
    counter = Counter(opponent_history)
    most_common = counter.most_common(1)[0][0]

    if most_common == "R":
        return "P"
    elif most_common == "P":
        return "S"
    else:
        return "R"

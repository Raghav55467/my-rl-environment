def grade(observation):
    # If the value reached 10, give a perfect score
    if observation.state.get("val") >= 10:
        return 1.0
    return 0.0

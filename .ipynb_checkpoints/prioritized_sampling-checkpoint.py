experience =namedtuple("Experience", field_names=["state", "action", "reward", "next_state", "done"])
e = experience(1, 1, [1.0], 1, 2)
e2 = experience(1, 1, [-1.0], 1, 2)
list_of_exps = [e, e2, e, e, e, e2, e, e2, e]
count_1 = len(list(filter(lambda x: x if x.reward[0] == 1.0 else None, list_of_exps)))
count_minus_1 = len(list(filter(lambda x: x if x.reward[0] == -1.0 else None, list_of_exps)))
count_0 = len(list(filter(lambda x: x if x.reward[0] == 0.0 else None, list_of_exps)))
# Hay que haceer el calculo pensando que puede no haber de uno de los casos --> habría que reponderar probabilididaes
count_1 + count_minus_1 + count_0
prob_1 = 0.7
prob_minus_1 = 0.2
prob_0 = 0.1

def assign_prob(exp):
    reward = exp.reward[0]
    if reward == 0.0:
        return prob_0/count_0
    elif reward == 1.0:
        return prob_1/count_1
    else:
        return prob_minus_1/count_minus_1

probabilities_vector = list(map(assign_prob, list_of_exps))
#np.random.choice(list(range(0, len(list_of_exps))), size=3, p=probabilities_vector)
# coding: utf-8


from functools import partial
from quiz import addn, list_dot, scalar_vect_mult


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [line.strip('\n').split(' ') for line in f]


def create_voting_dict(strlist):
    return {l[0]: [int(s) for s in l[3:]] for l in strlist}


def policy_compare(sen_a, sen_b, voting_dict):
    return list_dot(voting_dict[sen_a], voting_dict[sen_b])


def similarity(sen, voting_dict, which='least'):
    t = [(s, policy_compare(sen, s, voting_dict))
         for s in voting_dict if s != sen]
    ms = sorted(t, key=lambda x: x[1])
    w = -1 if which == 'most' else 0
    return ms[w][0]


most_similar = partial(similarity, which='most')
least_similar = partial(similarity, which='least')


def find_average_similarity(sen, sen_set, voting_dict):
    return sum(policy_compare(sen, s, voting_dict)
               for s in sen_set) / len(sen_set)


def find_average_record(sen_set, voting_dict):
    ac = [0] * len(voting_dict['Biden'])
    for k, v in voting_dict.items():
        if k in sen_set:
            ac = addn(ac, v)
    return scalar_vect_mult(1 / len(sen_set), ac)

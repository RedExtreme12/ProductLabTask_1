from collections import defaultdict


def create_dict_of_vectors_adjacency(
        network: tuple[tuple[str, str], ...],
) -> defaultdict[str | set[str, ...]]:
    """
    Creates dict that contains structures similar on adjacency vectors.
    Each vector contains people that adjacent (know each other) with other people.
    """
    dict_of_vectors_adjacency: defaultdict[str | set[str, ...]] = defaultdict(set)

    for pair_of_people in network:
        first_person, second_person = pair_of_people

        dict_of_vectors_adjacency[first_person].add(second_person)
        dict_of_vectors_adjacency[second_person].add(first_person)

    return dict_of_vectors_adjacency


def check_relation(
        network: tuple[tuple[str, str], ...],
        source_person: str,
        target_person: str,
) -> bool:
    dict_of_vectors_adjacency = create_dict_of_vectors_adjacency(network)

    stack = [source_person]
    visited_persons = set()

    while stack:
        person = stack.pop()

        if target_person in dict_of_vectors_adjacency[person]:
            return True
        else:
            not_visited_persons = filter(lambda person_: person_ not in visited_persons,
                                         dict_of_vectors_adjacency[person])  # Excluding loops

            stack.extend(not_visited_persons)

        visited_persons.add(person)

    return False

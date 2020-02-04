def create_sample_space(cards):
    sample_space = list(itertools.combinations(cards, 2))
    return sample_space

sample_space = create_sample_space(cards)

sample_space[0]

def random_variable(two_cards):
    """two cards will be tuple of tuples in the form (('diamonds', 'A'), ('diamonds', '3'))"""
    card1 = two_cards[0][1]
    card2 = two_cards[1][1]
    if card1 in royals:
        card1 = royals[card1]
    if card2 in royals:
        card2 = royals[card2]
    total = int(card1) + int(card2)
    return total

card_index = np.random.choice(len(sample_space), 1)[0]
print(sample_space[card_index])
random_variable(sample_space[card_index])


all_values = [random_variable(a) for a in sample_space]

counter = Counter(all_values)

pmf = {}
for key, val in counter.items():
    pmf[key] = (round(val / len(all_values), 4))

print(pmf)
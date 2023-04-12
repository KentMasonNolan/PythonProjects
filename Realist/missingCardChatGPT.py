import time
import timeit


def missing_card(cards):
    # create a set of all possible cards
    all_cards = set([f"{c}{v}" for c in ['S', 'H', 'D', 'C'] for v in
                     ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']])
    # create a set of cards in the given string
    given_cards = set(cards.split())
    # return the difference between the two sets, which will be the missing card
    return (all_cards - given_cards).pop()


missing_card("S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA D2 D3 D4 D5 D6 D7 D8 D9 "
             "D10 DJ DQ DK DA C2 C3 C4 C5 C7 C8 C9 C10 CJ CQ CK CA")

print(timeit.timeit(stmt='missing_card("S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK '
                         'HA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA C2 C3 C4 C5 C7 C8 C9 C10 CJ CQ CK CA")',
                    setup='from __main__ import missing_card', timer=time.perf_counter, number=500000, globals=None))
# ChatGPT
# 1.4499993994832039e-05

# Kent's code
#1.479999627918005e-05
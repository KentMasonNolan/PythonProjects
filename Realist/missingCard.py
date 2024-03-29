import struct
import time
import timeit


def missing_card(cards):
    defaultCards = "S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA D2 D3 " \
                   "D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK CA"

    defaultCardsArr = str.split(defaultCards)
    defaultCardsList = set(defaultCardsArr)
    cardsArr = str.split(cards)
    cardsList = set(cardsArr)
    missing = (set(defaultCardsList.difference(cardsList)))
    missingString = "".join(missing)
    return missingString


missing_card("S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA D2 D3 D4 D5 D6 D7 D8 D9 "
             "D10 DJ DQ DK DA C2 C3 C4 C5 C7 C8 C9 C10 CJ CQ CK CA")


print(timeit.timeit(stmt='missing_card("S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK '
                         'HA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA C2 C3 C4 C5 C7 C8 C9 C10 CJ CQ CK CA")',
                    setup='from __main__ import missing_card', timer=time.perf_counter, number=500000, globals=None))

#1.479999627918005e-05

# 2.728593699983321


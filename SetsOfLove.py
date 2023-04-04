def love_meet(bob, alice):
    bob = set(bob)
    alice = set(alice)
    meetingLocations = set(bob.intersection(alice))
    print(meetingLocations)
    return meetingLocations

def affair_meet(bob, alice, silvester):

    bob = set(bob)
    alice = set(alice)
    silvester = set(silvester)

    possibleMeetingLocations = set(alice.intersection(silvester))
    affairLocatons = set(possibleMeetingLocations.difference(bob))
    print(affairLocatons)
    return affairLocatons

    # defaultCardsList = set(defaultCardsArr)
    # cardsArr = str.split(cards)
    # cardsList = set(cardsArr)
    # missing = set(defaultCardsList.difference(cardsList))
    # missingString = "".join(missing)
    # return missingString


alice = ['Ⅱ', 'Ⅳ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅱ']
bob = ['Ⅳ', 'Ⅲ', 'Ⅱ', 'ⅩⅩ', 'Ⅱ', 'ⅩⅩ']
silvester = ['ⅩVⅢ', 'ⅩⅠⅩ', 'Ⅲ', 'Ⅰ', 'Ⅲ', 'ⅩVⅢ']

love_meet(bob, alice)
affair_meet(bob, alice, silvester)
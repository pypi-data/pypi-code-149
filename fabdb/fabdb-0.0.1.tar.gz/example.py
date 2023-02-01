from fabdb.client import FabDBClient

client = FabDBClient()

print("Single card by ID:")
nimblism = client.get_card("nimblism-yellow")
print(nimblism.name)
print()


print("Search Cards:")
ranger_cards = client.search_cards(class_="ranger", pitch=2)
for c in ranger_cards:
  # automatically handles requesting additional pages as needed
  print(c)
print()


print("Find a deck:")
deck = client.get_deck("bYDmozyB")
print(deck.name)
print(deck.cards[0])

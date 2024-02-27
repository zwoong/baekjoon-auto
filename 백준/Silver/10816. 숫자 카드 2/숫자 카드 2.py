num_cards = int(input())
cards = list(map(int, input().split()))

num_checks = int(input())
check_cards = list(map(int, input().split()))

card_counts = {}

for card in cards:
    if card in card_counts:
        card_counts[card] += 1
    else:
        card_counts[card] = 1
      
result = [card_counts[card] if card in card_counts else 0 for card in check_cards]

print(*result)

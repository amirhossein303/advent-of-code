with open("inputs/day4.txt") as file:
	puzzle = file.read().strip()


scrathcards = [0 for _ in range(250)]
result = 0
for i, card in enumerate(puzzle.split("\n"), 1):
	scrathcards[i] += 1
	winning_numbers, numbers = [{int(num) for num in part.split()} for part in card.split(':')[1].split("|")]
	wnumbers = numbers.intersection(winning_numbers)
	if wnumbers:
		result += 2**(len(wnumbers)-1)
	for _ in range(scrathcards[i]):
		for j in range(len(wnumbers)):
			scrathcards[j+i+1] += 1

print("Part one:", result)
print("Part two:", sum(scrathcards))

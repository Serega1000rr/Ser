start1 = ["fee", "fie", "foe"]
rhymes = [
("flop", "get a mop"),
("fope", "turn the rope"),
("fa", "get your ma"),
("fudge", "call the judge"),
("fat", "pet the cat"),
("fog", "walk the dog"),
("fun", "say we're done"),
]
start2 = "Someone better"
for (first,second) in rhymes:
	for n in range(len(start1)):
		print(start1[n].capitalize(), '! ', first.capitalize(),'! ', end=' ')
	print()
	print(start2,' ', second, '.')

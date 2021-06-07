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
start_cap=' '.join([word.capitalize()+'!' for word in start1])
for (first,second) in rhymes:
	print(f'{start_cap} {first.capitalize()}!')
	print(start2 , second+'.')
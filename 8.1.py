e2f={'dog':'chien','cat':'chat','walrus':'morse'}
print(e2f['walrus'])
f2e={fr:en for en,fr in e2f.items()}
print(f2e['chien'])
print(set(f2e.keys()))
life={
'animals':{
	'cats':['Henri','Grumpy','Lucy'],
	'octopi':{},
	'emus':{},
},
'plants':{},
'other':{}
}
print(life.keys())
print(life['animals'].keys())
print(life['animals']['cats'])
squares = {number:number*number for number in range(10)}
odd= [ number for number in range(10) if number% 2 ==1]
print(odd)
new = zip(('optimist', 'pessimist', 'troll'),('The glass is half full', 'The glass is half empty', 'How did you get a glass?'))
new1=dict(new)
print(new1)
titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']
moves = dict(zip(titles,plots))
print(moves)
for thing in ('Got %s' % number for number in range(10)):
	print(thing)
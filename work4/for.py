# в цикле for in , print выводится после четырех отступов

magicians = ['alice', 'david', 'carolina']
for magic in magicians:
    print(magic)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician. title() + ".\n")

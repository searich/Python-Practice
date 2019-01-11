formatter = '{} {} {} {}'

print(formatter.format(1, 2, 3, 4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(
    formatter.format("Try your", "Own text here", "Maybe a poem",
                     "Or a song about fear")
      )

# Here is some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print('''
    There's something going on here.
    With the three double-quotes.
    We'll be able to type as much as we like.
    Even 4 lines if we want, or 5, or 6.
''')

age = input("How old are you?")
height = input("How tall are you?")
weight = input("How much do you weigh?")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

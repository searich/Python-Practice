vowels = ['a', 'e', 'i', 'o', 'u']
phrase = input('Provide a phrase to search for vowels: ')
found = {}
# # found['a'] = 0
# # found['e'] = 0
# # found['i'] = 0
# # found['o'] = 0
# # found['u'] = 0
for key in phrase:
    if key in vowels:
        found.setdefault(key, 0)
        found[key] += 1
for k, v in sorted(found.items()):
    print(f'{k} was found {v} time(s)')
# for key in phrase:
#         if key in vowels:
#             found.setdefault(key, 0)
#             found[key] += 1
# # for key in sorted(found):
# #    if found[key] != 0:
# #        print(key, found[key])

# for k, v in sorted(found.items()):
#     # if v != 0:
#     print(f'{k} was found {v} time(s).')

vowels = set('aeiou')
input_words = input('your words: ')
words = set(input_words)
found = vowels.intersection(words)

for w in sorted(found):
    print(w)

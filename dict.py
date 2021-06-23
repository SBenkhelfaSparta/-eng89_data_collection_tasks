story1 = {
    'start': 'Once upon a time...',
    'middle': '...and...',
    'end': '... the end.',
}
print(story1)
print(type(story1))
print(story1.keys())
print(story1.values())

for story in story1.values():
    print(story)

story1['hero'] = "Link"
print(story1)
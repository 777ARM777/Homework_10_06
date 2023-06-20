formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))                             # in place of each {} puts 1, 2, 3, 4
print(formatter.format("one", "two", "three", "four"))          # in place of each {} puts "one", "two", "three", "four"
print(formatter.format(True, False, False, True))               # in place of each {} puts True, False, False, True
print(formatter.format(formatter, formatter, formatter, formatter)) # in place of each {} puts {} {} {} {}
print(formatter.format("Try your", "Own text here", "Maybe a poem", "Or a song about fear"))
# # in place of each {} puts "Try your", "Own text here", "Maybe a poem", "Or a song about fear"

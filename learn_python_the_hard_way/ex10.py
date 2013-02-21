tabby_cat = "\tI'm tabbed"
persian_cat = "I am split\non a line"
backslash_cat = "I am \\ a \\ cat"
fat_cat = """
I'll do a list"
\a*cat food
\t*fishes
\t*Catnip\n\t*grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,

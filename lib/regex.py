import re


# "It's such a lovely day today."
# "Some weather we're having today."
# "Maybe today's just not my day."
my_pattern = r""
my_regex = re.compile(my_pattern)
my_regex = re.compile(r"It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\.")



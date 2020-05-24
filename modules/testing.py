from nlp import Text
string = """
Hello, welcome to my world. You are very much welcome.
"""
string_0 = """
We resolve to be brave. We resolve to be good. We resolve to uphold the law according to our oath.
"""
substring = "resolve"
replacement = "HOLA"
num = 3

print(Text().find_and_replace(string_0, substring, replacement, num))
# Text().find_and_replace(string, substring, replacement, num)
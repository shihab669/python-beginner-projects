#We need to install demoji using 'pip install demoji'

import demoji

text = "we are removing emoji from this sentence! 🎉🥳"


removed_text = demoji.replace(text, "")

print(removed_text)

# We can also replace Emojis with Descriptive Text

text_2 = "We are removing emoji from this sentence 🎂🎈"

removed_text2 = demoji.replace_with_desc(text)

print(removed_text2)
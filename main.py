# Remove empty strings from a list of Strings in Python

my_list = ['bobby', '', 'hadz', '', 'com', '']

new_list = [item for item in my_list if item]
print(new_list)  # 👉️ ['bobby', 'hadz', 'com']
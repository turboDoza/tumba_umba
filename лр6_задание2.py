text = "стеклянный, оловянный, деревянный."
consonants = 'бвгджзйклмнпрстфхцчшщ'
words = []
current_word = ''
count = 0

for char in text:
    if char.isalpha():
        current_word += char
    else:
        if current_word:
            words.append(current_word)
            current_word = ''
            
if current_word:
    words.append(current_word)

for word in words:
    for i in range(1, len(word)):
        if word[i] == word[i - 1] and word[i] in consonants:
            count += 1
            break 

print("Количество слов с удвоенной согласной:", count)
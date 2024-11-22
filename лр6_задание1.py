text = input("Введите текст: ")

count = 0
current_word = ''

for char in text:
    if char.isalpha(): 
        current_word += char  
    else:
        if current_word: 
            count += 1  
            current_word = ''  

if current_word:
    count += 1

print("Количество слов в тексте:", count)
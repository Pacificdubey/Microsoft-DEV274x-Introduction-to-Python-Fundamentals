def word_mixer(word_list):
    new_list = []
    word_list.sort()
    
    while len(word_list) > 5:
        new_list.append(word_list.pop(-5))
        new_list.append(word_list.pop(0))
        new_list.append(word_list.pop(-1))
    return new_list
    

# getting input from user
poem = input("Enter a saying or poem:")
word_list = poem.split()
for index in range(0,len(word_list)):
    if len(word_list[index]) < 4:
        word_list[index] = word_list[index].lower()
    elif len(word_list[index]) >= 7:
        word_list[index] = word_list[index].upper()  
        
# calling function with modified list
a = word_mixer(word_list)
print(' '.join(a))

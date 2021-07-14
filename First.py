#if it starts with a vowel, add yay. Ex: eat -> eatyay
#if it stars with a consonant, send the first consonant cluster to the back of the word and add ay. Ex: pig -> igpay

#get sentence from user

original = input("Please enter a sentece: ").strip().lower()

#split sentence into words

words = original.split()
print(words)
#loop through words and convert to pig latin

new_words = [] #blank list

#if starts with vowel, just add "yay"
#otherwise, move the first consonant cluster to end, and add "ay"

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0 #de vowel position
        for letter in word: 
            if letter not in "aeiou": #if it isn't a vowel, then it's a consonant (actually, it could be other symbols like %$# but I'm too lazy to fix this) 
                vowel_pos = vowel_pos + 1                     
            
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:] # everything after the consonant cluster
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)


        


#stick words back together
output = " ".join(new_words) 

#output the final string

print(output)

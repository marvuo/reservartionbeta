def break_words(mystring):
    new_text = mystring.split(' ')
    return new_text

def return_first_text(mystring):
    new_text = mystring.pop(0)
    return new_text

def reverse_text(mystring):
    new_text = sorted(mystring, reverse = True)
    return new_text
    
def sorted_word(mystring):
    return sorted(mystring)


original_text = "this is very long and boring text"

text_list = break_words(original_text)

print return_first_text(sorted(text_list))
print reverse_text(text_list)

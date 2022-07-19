import json
from difflib import get_close_matches

data = json.load(open('dict_data.json'))

def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        newWord = get_close_matches(word, data.keys())[0]
        choice = input(f'Did you mean "{newWord}" instead? \nEnter "Y" if yes else "N" if no: ')
        
        if choice in ['y', 'Y', 'Yes', 'yes']:
            return data[newWord]
        elif choice in ['n', 'N', 'No', 'no']:
            return f'The Word "{word}" does not exist, Please Recheck your word!'
        else:
            return f"Sorry we didn't understand you answer!."

if __name__=='__main__':
    word = input('Enter the Word: ')
    final_output = meaning(word)
    if type(final_output) == list:
        num = 1
        for output in final_output:
            print(f'{num}) - {output}')
    else:
        print(final_output)


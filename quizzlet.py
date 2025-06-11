def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    

    # print something if the answer is correct
    # assum all eight questions will be asked -- EXTENTION: keep track of how many questions w

    num_correct_answer = 0
    num_total_question = 0

    for key in translations:
        user_got_it_right = ask_quiz_word(key, translations[key])
        
        if user_got_it_right:
            print_when_correct()

        else:
            print_when_not_correct(key, translations[key])

        print()

        # keep count of how many the user gets correct

        num_correct_answer += user_got_it_right
        num_total_question += 1


        #print(translations[key])

    print("You got " + str(num_correct_answer) + "/" + str(num_total_question) + " words correct, come study again soon!")

def ask_quiz_word(word_to_ask, correct_answer):
    answer_the_user_gave = input("What is the Spanish translation for " + word_to_ask + "? ")

    if answer_the_user_gave == correct_answer:
        return True

    else:
        return False


def print_when_correct():
    # print somenthing if the answer is correct
    print("That is correct!")


def print_when_not_correct(basa_word, translation_of_the_word):
    # print somenthing if its not correct
    print("That is incorrect, the Spanish translation for " + basa_word + " is " + translation_of_the_word + ".")

if __name__ == '__main__':
    main()
#You have a list of words.
#When the file opens, you have 3 seconds to provide a translation of the word.
#It then reveals the translation.
#If you answer correctly, user clicks tick and the word gets removed from the list.
#If you don't answer correctly, user clicks cross and the word goes back into the list.
#Once there are no more words in the list, the program closes, otherwise, it keeps going.


################################## INITIAL ENTRIES #################################
BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from tkinter import messagebox
import json
import pandas as pd

import random
learn_words = "C:/Users/Asanka/Desktop/Python Practice/flash-card-capstone/data/learn_french.csv"
word_list = pd.read_csv("C:/Users/Asanka/Desktop/Python Practice/flash-card-capstone/data/french_words.csv", header=None, index_col=0)
word_list = word_list[1]
del(word_list["French"])
json_wordlist = "C:/Users/Asanka/Desktop/Python Practice/flash-card-capstone/data/french_words.json"
output = word_list.to_json(json_wordlist, indent = 4)
decoded_output = json.dumps(output, ensure_ascii=False).encode('utf8')
learn_list = "C:/Users/Asanka/Desktop/Python Practice/flash-card-capstone/data/words_to_learn.json"
with open(json_wordlist, "r") as data:
    store = json.load(data)
import csv
################################## USER INTERFACE ##################################

window = Tk()
window.title("Flashy")
window.config(padx=100, pady=100, bg=BACKGROUND_COLOR)
canvas=Canvas(width=900,height=700, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image=PhotoImage(file="C:/Users/Asanka/Desktop/Python Practice/flash-card-capstone/images/card_front.png")
right_image=PhotoImage(file="C:/Users/Asanka/Desktop/Python Practice/flash-card-capstone/images/right.png")
wrong_image=PhotoImage(file="C:/Users/Asanka/Desktop/Python Practice/flash-card-capstone/images/wrong.png")
back_image=PhotoImage(file="C:/Users/Asanka/Desktop/Python Practice/flash-card-capstone/images/card_back.png")
background = canvas.create_image(468,300,image=front_image)
canvas.grid(row=0, column=0, columnspan=2)
lang_text = canvas.create_text(468, 200, text = "French", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(468, 350, text = "Word", fill="black", font=("Ariel", 60, "bold"))

########################################### BUTTONS #################################

def incorrect():
    word_learn = {french_word : english_word}

    try:

        with open(learn_list, "r") as data:
            words = json.load(data)
    
    except FileNotFoundError:

        with open(learn_list, "w") as data:
            json.dump(word_learn, data, indent=4)
    
    else:
        if french_word not in learn_list:
            words.update(word_learn)
            with open(learn_list, "w") as data:
                json.dump(words, data, indent=4)
        
    finally:
        window.after_cancel(time)
        first_screen()

def correct():   

    del store[french_word]
    window.after_cancel(time)
    first_screen()

right_button=Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=correct)
wrong_button=Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=incorrect)
right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

################################## SCREEN FUNCTIONALITY ########################################
def first_screen():
    
    global time
    if not store:
        window.quit()
    else:
        global french_word
        global english_word
        canvas.itemconfig(background, image = front_image)
        french_word = random.choice(list(store.keys()))
        english_word = store[french_word]
        canvas.itemconfig(lang_text, text="French")
        canvas.itemconfig(word_text, text=f"{french_word}")
        time = window.after(3000, second_screen)

        
            
def second_screen():
    canvas.itemconfig(background, image = back_image)
    canvas.itemconfig(lang_text, text="English")
    canvas.itemconfig(word_text, text=f"{english_word}")


first_screen()



  


window.mainloop()
        

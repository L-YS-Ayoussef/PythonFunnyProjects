from tkinter import *
import pandas
import random
from tkinter import messagebox

tik_tok = None
word_fr_en_dict = {}
words_to_learn = []

data = pandas.read_csv("french_words.csv")
data_dict = data.to_dict(orient="records")  # note 2


# -----------------> PROGRAM MECHANISM ---------------------------<
def french_words():
    global tik_tok, word_fr_en_dict
    if len(data_dict) != 0:
        word_fr_en_dict = random.choice(data_dict)
        word_french = word_fr_en_dict["French"]

        canvas_lang1.itemconfig(image, image=image_canvas_lang1)
        canvas_lang1.itemconfig(title, text="French")
        canvas_lang1.itemconfig(word, text=word_french)

        tik_tok = window.after(3000, english_words)
    else:
        messagebox.showinfo(
            title="Congratulations!",
            message="Congratulations!\nYou have finished the words correctly",
        )


def english_words():
    global word_fr_en_dict
    word_english = word_fr_en_dict["English"]

    canvas_lang1.itemconfig(image, image=image_canvas_lang2)
    canvas_lang1.itemconfig(word, text=word_english)
    canvas_lang1.itemconfig(title, text="English")

    window.after_cancel(tik_tok)


def right_answer():
    words_to_learn.append(word_fr_en_dict)
    data_dict.remove(word_fr_en_dict)
    french_words()


def finish():
    words_learn = pandas.DataFrame(words_to_learn)
    words_learn.to_csv("words_to_learn.csv", index=False)

    result = messagebox.askokcancel(
        title="Show Learned Words", message="Do you want to show the learned words? "
    )
    if result:
        learned_words = pandas.read_csv("words_to_learn.csv")

        if learned_words.empty:
            messagebox.showinfo(
                title="No learned words",
                message="You haven't marked any words as learned yet.",
            )
            return

        window1 = Toplevel(window)
        window1.title("Learned Words")
        window1.config(bg="#B1DDC6")
        window1.resizable(False, False)
        icon_image2 = PhotoImage(master=window1, file="right.png")
        window1.iconphoto(False, icon_image2)
        window1.icon_image = icon_image2

        label1 = Label(window1, text="FRENCH", font=("Ariel", 20, "bold"), bg="#B1DDC6")
        label1.grid(row=0, column=0)
        label2 = Label(
            window1, text="ENGLISH", font=("Ariel", 20, "bold"), bg="#B1DDC6"
        )
        label2.grid(row=0, column=2)

        # display learned words as a table (one word per row)
        for idx, row_data in learned_words.iterrows():
            row_num = idx + 1

            l_french = Label(
                window1,
                text=row_data["French"],
                font=("Ariel", 15, "normal"),
                bg="#59E0D4",
                anchor="w",
                width=20,
            )
            l_french.grid(row=row_num, column=0, padx=5, pady=2, sticky="w")

            l_english = Label(
                window1,
                text=row_data["English"],
                font=("Ariel", 15, "normal"),
                bg="#2659D6",
                anchor="w",
                width=20,
            )
            l_english.grid(row=row_num, column=2, padx=5, pady=2, sticky="w")

    else:
        window.destroy()


# --------------------> UI (USER INTERFACE) ----------------------<
# WINDOW
window = Tk()
window.title("FLASH CARD")
window.config(padx=50, pady=50, bg="#B1DDC6")
window.resizable(False, False)
icon_image = PhotoImage(file="right.png")
window.iconphoto(False, icon_image)
window.icon_image = icon_image

# CANVAS
image_canvas_lang1 = PhotoImage(file="card_front.png")
image_canvas_lang2 = PhotoImage(file="card_back.png")

canvas_lang1 = Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)
image = canvas_lang1.create_image(400, 263, image=image_canvas_lang1)
title = canvas_lang1.create_text(
    400, 200, text="", fill="black", font=("Ariel", 40, "italic")
)
word = canvas_lang1.create_text(
    400, 312, text="", fill="black", font=("Ariel", 60, "bold")
)
canvas_lang1.grid(row=0, column=0, columnspan=2)

# BUTTONS
image_right = PhotoImage(file="right.png")  # NOTE 3
right = Button(image=image_right, highlightthickness=0, command=right_answer)
right.grid(row=1, column=1)

image_wrong = PhotoImage(file="wrong.png")
wrong = Button(image=image_wrong, highlightthickness=0, command=french_words)
wrong.grid(row=1, column=0)

finish_button = Button(
    text="Finish",
    bg="#B1DDC6",
    highlightthickness=0,
    command=finish,
    width=15,
    height=5,
)
finish_button.config(font=("Ariel", 10, "bold"))
finish_button.grid(row=2, column=0, columnspan=2)


french_words()
window.mainloop()

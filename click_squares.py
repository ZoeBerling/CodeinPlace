"""
File: click_squares.py
----------------
YOUR DESCRIPTION HERE
This code was created without the knowledge of Classes, so it is extremely ugly.
I also gave up on trying to save color changes in lists, so the mouse click
function is on pause until I can figure that out.
Other than that, this is a rough play on the Humble-Nishiyama Randomness Game
The game picks 4 red and black cards,
You pick 4 red and black cards,
If your sequence of red and black cards appears in the deck first, you win
You are player 2, so you have a strategic advantage.
"""


import tkinter
import time
import random
import functools
from PIL import ImageTk
from PIL import Image

CANVAS_WIDTH = 750      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 800     # Height of drawing canvas in pixels
NUM_CARDS = 4


def main():
    """ Game Set Up: create and shuffle deck, define player 1's cards"""
    # define card order in deck
    card_deck = []
    for cards in range(26):
        card_deck.append('black')
        card_deck.append('red')
    random.shuffle(card_deck)
    # print(card_deck)
    # player 1 cards as a list
    player_cards = []
    # randomly select player 1 cards
    for c in range(NUM_CARDS):
        player_cards.append(random.choice(['black', 'red']))

    """Board Set Up: create canvas for playing cards and list_fill default cards"""
    # UI
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Game Board')
    # list for player 2 cards
    list_fill_2 = []
    welcome_sequence(canvas)

    """Show player 1 cards"""
    # create player 1 cards on canvas
    for col in range(len(player_cards)):
        draw_square(canvas, col, player_cards)

    canvas.update()
    time.sleep(1)

    # create player 2 cards on canvas
    player_2(canvas, list_fill_2, player_cards)
    # print(list_fill_2)

    canvas.update()
    time.sleep(2)
    # create deck

    """Play Game: draw first four cards from deck"""
    drawn_cards = []
    discard_cards = []
    for drawn in range(4):
        take_card = card_deck.pop()
        drawn_cards.append(take_card)
    # print(drawn_cards)
    deck(canvas, drawn_cards)
    # canvas.update()
    # time.sleep(3)

    """draw cards while updating deck"""
    # compare(player_2, player_cards, drawn_cards)
    while len(card_deck) > 0:
        canvas.update()
        time.sleep(2)
        if compare(list_fill_2, player_cards, drawn_cards) is False:
            take_card = card_deck.pop()
            drawn_cards.append(take_card)
            x = drawn_cards.pop(0)
            discard_cards.append(x)
            deck(canvas, drawn_cards)

            # print(drawn_cards)
        else:
            count = len(discard_cards) + 4
            count_text = "There were " + str(count) + " cards drawn."
            canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, fill='blue', font='Arial 30 bold', text=count_text)
            canvas.update()
            time.sleep(3)

            if player_cards == drawn_cards:
                you_lose = "You lost."
                canvas.create_text(CANVAS_WIDTH / 2, (CANVAS_HEIGHT / 2) + 50, fill='turquoise', font='Arial 50 bold',
                                   text=you_lose)
                canvas.update()
                time.sleep(5)
            if list_fill_2 == drawn_cards:
                you_win = "You won!"
                canvas.create_text(CANVAS_WIDTH / 2, (CANVAS_HEIGHT / 2) + 50, fill='lime green', font='Arial 50 bold',
                                   text=you_win)
                canvas.update()
                time.sleep(5)

            card_deck.clear()

    # print(len(card_deck))
    # print(len(discard_cards) + 4)
    thanks = ImageTk.PhotoImage(Image.open("project images/export-0005.jpg"))
    canvas.create_image(0, 0, anchor="nw", image=thanks)
    canvas.update()
    # pause
    time.sleep(60)

    # canvas.mainloop()

""" definitions here!"""


def welcome_sequence(canvas):
    image = ImageTk.PhotoImage(Image.open("project images/export-0001.jpg"))
    image_2 = ImageTk.PhotoImage(Image.open("project images/py project 1 0001.png"))
    image_3 = ImageTk.PhotoImage(Image.open("project images/export-0002.jpg"))
    canvas.create_image(0, 0, anchor="nw", image=image)
    canvas.update()
    time.sleep(6)
    canvas.create_image(0,0, anchor="nw", image=image_2)
    canvas.update()
    time.sleep(6)
    canvas.create_image(0, 0, anchor="nw", image=image_3)
    time.sleep(3)


def check_entry(list_fill_2, player_cards, canvas):
    if list_fill_2 != player_cards:
        return list_fill_2
    else:
        while list_fill_2 == player_cards:
            time.sleep(1)
            print("Please choose different cards than Player 1 ")
            list_fill_2.clear()
            time.sleep(1)
            player_2(canvas, list_fill_2, player_cards)
        return list_fill_2


# Bool for results: true if winner, false if no winner
def compare(list_fill_2, player_cards, drawn_cards):
    if list_fill_2 == drawn_cards:
        # print("Player 2 Wins!")
        # print(drawn_cards)
        return True
    elif player_cards == drawn_cards:
        # print("Player 1 Wins!")
        # print(drawn_cards)
        return True
    else:
        # print("False")
        return False


def deck(canvas, draw_cards):
    x = CANVAS_WIDTH / 1.2
    y = CANVAS_HEIGHT - 60
    arrow = ImageTk.PhotoImage(Image.open("project images/arrow.png"))
    arrow_image = canvas.create_image(x, y, anchor="se", image=arrow)
    t = time.time() + 1
    while time.time() < t:
        canvas.move(arrow_image, -15, 0)
        canvas.update()
        time.sleep(1 / 50)

    for col in range(4):
        draw_deck(canvas, col, draw_cards)


def ask(col):
    print("What color do you think card #" + str(col + 1) + " will be?")
    color = input(("Please choose red or black: "))
    if color == "red" or color == "black":
        return color
    while color != 'red' and color != 'black':
        print("Invalid response")
        color = input("Please only choose red or black: ")
    return color


def draw_deck(canvas, col, draw_cards):

    width = 160
    height = 250
    fill_color = draw_cards[col]
    x = col * (CANVAS_WIDTH / 4)
    y = CANVAS_HEIGHT - (height + 5)

    canvas.create_rectangle(x, y, x + width, y + height, fill=fill_color, outline='white')


# create cards for player 2
def player_2(canvas, list_fill_2, player_cards):
    for col in range(4):
        draw_square_2(canvas, col, list_fill_2)
    check_entry(list_fill_2, player_cards, canvas)


# define player 2 card dimension and colors
def draw_square_2(canvas, col, list_fill_2):
    width = 120
    height = 170
    fill_color = ask(col)
    x = (col * CANVAS_WIDTH / 6)
    y = height + 20
    canvas.create_rectangle(x, y, x + width, y + height, fill=fill_color, outline='white')
    list_fill_2.append(fill_color)


# define player 1 cards dimension and colors
def draw_square(canvas, col, player_cards):
    width = 120
    height = 170
    fill_color = player_cards[col]
    x = (col * CANVAS_WIDTH / 6)
    y = 0
    text_1 = "<== Player 1 cards."
    text_2 = "Choose your colors in the terminal"
    text_3 = "<== Your cards."
    canvas.create_rectangle(x, y, x + width, y + height, fill=fill_color, outline='white')
    canvas.create_text(width * 5.3, height / 2, fill='black', font='Arial 18 bold', text=text_1)
    canvas.create_text(width * 2, height * 1.5, fill='black', font='Arial 20 bold', text=text_2)
    canvas.create_text(width * 5.3, height * 1.5, fill='black', font='Arial 20 bold', text=text_3)


""" def change_color_red(canvas, found, color):
    canvas.itemconfig(found, fill='red')
    # list_fill_2.append(color)
    # print(list_fill_2)"""

# Come back to this later: it would be cool if the mouse click changed the color instead of the terminal
"""def mouse_pressed(event, canvas):
    print('mouse pressed', event.x, event.y)
    x = event.x
    y = event.y
    found = canvas.find_overlapping(x, y, x, y)
    # change color of card to either red or black
    if len(found) > 0:
        color = canvas.itemcget(found, "fill")
        if color == 'green':
            canvas.itemconfig(found, fill='red')
        if color == 'red':
            canvas.itemconfig(found, fill='black')
        if color == 'black':
            canvas.itemconfig(found, fill='red')
        if color == 'turquoise':
            canvas.itemconfig(found, fill='blue')"""


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    # canvas.bind("<Button-1>", lambda e: mouse_pressed(e,canvas))
    return canvas




if __name__ == '__main__':
    main()

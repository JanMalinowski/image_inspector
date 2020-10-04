import pandas as pd
from numpy import ceil
from ipywidgets import Button, Layout, GridspecLayout, Image, Output, Button, ToggleButton
from IPython.display import display



def display_image(
    out,
    path,
    imgs,
    iterator,
    ):
    # A simple function for displaying images. using ipywidget's out allows us
    # to change the output dynamically
    with out:
        out.clear_output()
        file = open(path + '/' + imgs[iterator], 'rb')
        image = file.read()
        display(Image(value=image, width=400, height=400)) 

def create_button(description, cb, disabled=False):
    button = Button(description=description, disabled=disabled,
                            button_style='')
    #Adding the  on-click callback
    button.on_click(cb)
    return button


def create_toggle_button(description):
    button = ToggleButton(value=False, description=description,
                                  disabled=False)
    return button

def next_wrapper(
    next_button,
    prev_button,
    iterator,
    imgs,
        ):
    # Disabling the button when the iterator 
    # reaches the last image
    if iterator == len(imgs) - 2:
        next_button.disabled = True
        iterator = iterator + 1
    elif iterator >= len(imgs) - 1:
        next_button.disabled = True
    else:
        iterator = iterator + 1
    
    # After clicking the next_buton the prev_button
    # Should no longer be disabled
    if prev_button.disabled:
        prev_button.disabled = False

    return (next_button, prev_button, iterator)


def prev_wrapper(
    next_button,
    prev_button,
    iterator,
    imgs,
        ):
    # If we move to the 0th image, it's no longer possible
    # to move back
    if iterator == 1:
        prev_button.disabled = True
        iterator = iterator - 1
    elif iterator < 1:
        prev_button.disabled = True
    else:
        iterator = iterator - 1
    
    # If the next_button was disabled, clicking the prev_button
    # should change disabled to False
    if next_button.disabled:
        next_button.disabled = False

    return (next_button, prev_button, iterator)

    # A simple class for creating a grid of toggle buttons
# It has some additional utilities such as
# get_values or load_values methods
class ToggleGrid:

    def __init__(self, categories, n_cols=3):
        self.cats = categories
        self.n_cols = n_cols
        self.n_rows = int(ceil(len(self.cats) / n_cols))
        self.grid = GridspecLayout(self.n_rows, self.n_cols)
    
    # The grid gets created on calling the class
    def __call__(self):
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.n_cols * i + j <= len(self.cats) - 1:
                    self.grid[i, j] = \
                        create_toggle_button(self.cats[self.n_cols * i + j])
        return self.grid

    # get_values method takes the current buttons' values and resets the buttons
    def get_values(self):
        values = list()

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.n_cols * i + j <= len(self.cats) - 1:
                    values.append(self.grid[i, j].value)
                    self.grid[i, j].value = False
        return values

    # load_values method sets the buttons' loads buttons'
    # previous values, which are stored in the dataframe df
    def load_values(self, iterator, df):
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.n_cols * i + j <= len(self.cats) - 1:
                    self.grid[i, j].value = df.iloc[iterator, self.n_cols * i + j]
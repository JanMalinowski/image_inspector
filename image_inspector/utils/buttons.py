import pandas as pd
from numpy import ceil
from ipywidgets import Button, Layout, GridspecLayout, Image, Output, \
    Button, ToggleButton
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

    # Adding the  on-click callback

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

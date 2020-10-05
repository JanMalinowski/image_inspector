from ..utils.buttons import create_button, next_wrapper, prev_wrapper, \
    display_image
import pandas as pd
from ipywidgets import AppLayout, Output
from ..utils.toggle_grid import ToggleGrid
from IPython.display import display


# A class for inspecting the dataset.

class ImageInspector:

    def __init__(
        self,
        imgs,
        path,
        categories,
        n_cols=3,
        ):

        # list of images

        self.imgs = imgs

        # path to the folder containing the images

        self.path = path

        # list of categories.

        self.cats = categories
        self.iterator = 0

        # out_img stores the image that is being displayed.

        self.out_img = Output()

        # Creating the navigation buttons

        self.next = create_button('Next', self.next_click)
        self.prev = create_button('Previous', self.prev_click,
                                  disabled=True)
        self.grid = ToggleGrid(self.cats, n_cols=n_cols)

        # dataframe storing the results of the "inspection"

        self.result = pd.DataFrame(columns=self.cats)

    def __call__(self):
        display_image(self.out_img, self.path, self.imgs, self.iterator)

        # Creating the application layout

        app = AppLayout(header=None, left_sidebar=self.prev,
                        center=self.out_img, right_sidebar=self.next,
                        footer=self.grid())

        # displaying the application

        display(app)

    # Callback adding 1 to the iterator, loading a new image and saving the
    # data from the toggle grid to a dataframe

    def next_click(self, b):
        (self.next, self.prev, self.iterator) = next_wrapper(self.next,
                self.prev, self.iterator, self.imgs)
        display_image(self.out_img, self.path, self.imgs, self.iterator)

        values = self.grid.get_values()

        # writing the new values into a dataframe

        self.result.loc[self.iterator, :] = values

    # Callback subtracting 1 from the iterator, loading a previous image and
    # results for the previous image

    def prev_click(self, b):
        (self.next, self.prev, self.iterator) = prev_wrapper(self.next,
                self.prev, self.iterator, self.imgs)
        display_image(self.out_img, self.path, self.imgs, self.iterator)
        self.grid.load_values(self.iterator, self.result)
        
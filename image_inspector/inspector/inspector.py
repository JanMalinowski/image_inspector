from ..utils.buttons import create_button, next_wrapper, prev_wrapper, display_image
import pandas as pd
from ipywidgets import AppLayout, Output
from ..utils.toggle_grid import ToggleGrid
from IPython.display import display
from typing import List
import os


class ImageInspector:
    """
    A class for inspecting images through a simple
    IPywidgets GUI.

    :param imgs: list: of images' names
    :param path: path: to the folder with images
    :param categories: list of categories
    :param n_cols: list of columns of the toggle
    grid to be displayed
    """

    def __init__(
        self,
        path: str,
        categories: List[str],
        images: List[str] = None,
        n_cols: int = 3,
    ) -> None:

        # path to the folder containing the images
        self.path = path

        # list of categories.
        self.cats = categories
        self.iterator = 0

        # out_img stores the image that is being displayed.
        self.out_img = Output()

        # Creating the navigation buttons
        self.next = create_button("Next", self.next_click)
        self.prev = create_button("Previous", self.prev_click, disabled=True)
        self.grid = ToggleGrid(self.cats, n_cols=n_cols)

        # dataframe storing the results of the "inspection"
        self.result = pd.DataFrame(columns=self.cats + ["Image Name"])

        # list of images
        if images is None:
            self.imgs = os.listdir(path)
        else:
            self.imgs = images


    def __call__(self) -> None:
        display_image(self.out_img, self.path, self.imgs, self.iterator)

        # Creating the application layout
        app = AppLayout(
            header=None,
            left_sidebar=self.prev,
            center=self.out_img,
            right_sidebar=self.next,
            footer=self.grid(),
        )

        # displaying the application
        display(app)

    # Callback adding 1 to the iterator, loading a new image and saving the
    # data from the toggle grid to a dataframe
    def next_click(self, b) -> None:
        # reading the values from the toggle grid
        values = self.grid.get_values()

        # writing the new values into a dataframe
        self.result.loc[self.iterator, :] = values + [self.imgs[self.iterator]]

        (self.next, self.prev, self.iterator) = next_wrapper(
            self.next, self.prev, self.iterator, self.imgs
        )
        display_image(self.out_img, self.path, self.imgs, self.iterator)

    # Callback subtracting 1 from the iterator, loading a previous image and
    # results for the previous image
    def prev_click(self, b) -> None:
        (self.next, self.prev, self.iterator) = prev_wrapper(
            self.next, self.prev, self.iterator, self.imgs
        )
        display_image(self.out_img, self.path, self.imgs, self.iterator)
        self.grid.load_values(self.iterator, self.result)

    # Function returing a dataframe with the resuts.
    def get_results(self) -> pd.DataFrame:
        values = self.grid.get_values()

        self.result.loc[self.iterator, :] = values + [self.imgs[self.iterator]]
        self.grid.load_values(self.iterator, self.result)
        result = self.result.copy()
        result.index = result['Image Name']
        result = result.drop(['Image Name'], axis = 1)

        return result

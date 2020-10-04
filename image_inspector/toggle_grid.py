from buttons import create_toggle_button
from numpy import ceil
from ipywidgets import GridspecLayout

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
# Image_inspector

Image_inspector is a simple GUI application for data-inspection and/or labellig.
The ``` ImageInspector class``` helps label the data by displaying the image and a list of toggle-buttons below it. Once a toggle button is clicked, it set's the 
category corresponding to that button to True. Once the labelling is finished the data
can be accessed by callign the ```get_results()``` method

## Installation

The package can be installed by running the following command: 
```bash
!pip install git+git://github.com/JanMalinowski/image_inspector.git
```

## Usage
The class takes the following parameters:

```python
from image_inspector import ImageInspector

# imgs - list of images' names to be labelled
# path - path to the folder containing the images
# categories - list of the categories that the images may fall into

ii = ImageInspector(imgs=imgs, path=path, categories=categories) # Initializes ImageInspector class
ii() # Display's inspector's GUI
ii.get_results() # Return a data frame with the results
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
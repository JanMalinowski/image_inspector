# Image_inspector

Image_inspector is a simple GUI application for data-inspection and/or labellig.

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
# Image_inspector

Image_inspector is a simple GUI application for data-inspection and/or labelig.
The ``` ImageInspector``` class helps to label data by displaying an image and a list of toggle-buttons below it. Once a toggle button is clicked, it set's the 
category corresponding to that button to ```True```. Once the labeling is finished the data can be accessed by calling the ```get_results()``` .

## Video Tutorial

*Apologies for the sound quality*

https://youtu.be/Dxd0grCDlGE

## Installation

The package can be installed by running the following command: 
```bash
!pip install git+git://github.com/JanMalinowski/image_inspector.git
```

## Usage
Basic usage:

```python
from image_inspector import ImageInspector

# path - path to the folder containing the images
# categories - list of the categories that the images may fall into
# imgs - list of images' names to be labelled. [Optional]. If it's not specified
# then all of the images from the path directory will be used.


ii = ImageInspector(path=path, categories=categories, imgs=imgs) # Initializes ImageInspector class
ii() # Display's inspector's GUI
ii.get_results() # Return a data frame with the results
```
Additional examples can be found in this kaggle [kernel](https://www.kaggle.com/janmalin/simple-app-for-inspecting-the-dataset) or in this repo's examples directory.

## License
[MIT](https://choosealicense.com/licenses/mit/)
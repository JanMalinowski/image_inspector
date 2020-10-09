# Image_inspector

Image_inspector is a simple GUI application for data-inspection and/or labellig.

## Installation

The package can be installed by running the following command: 
```bash
!pip install git+git://github.com/JanMalinowski/image_inspector.git
```

## Usage

```python
from image_inspector import ImageInspector
ii = ImageInspector(imgs=imgs, path=path, categories=categories) # Initializes ImageInspector class
ii() # Display's inspector's GUI
ii.get_results() # Return a data frame with the results
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
PyColor
========

Module to print to the terminal in color with python!

Usage 
--------
```python
from PyColor import PyColor

print PyColor.GREEN + 'This is green!' + PyColor.DEFAULT
```

You may also get a line of colored text to use later:
```python

text = "I am successful!"
statusText = PyColor.getColorText(PyColor.GREEN, text)
print statusText
```

Or use the function to print it for you:
```python
text = "I am successful!"
statusText = PyColor.printColorText(PyColor.GREEN, text)
```
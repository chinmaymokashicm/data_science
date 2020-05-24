"""
Data pre-processing functions 
for machine learning
"""


class PreProcessing:
    # Importing necessary modules
    def import_modules(self, *args, **kwargs):
        list_code = [
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "import pandas as pd",
        "from IPython.display import display, Markdown, Latex" ]
        list_final_string = []
        for item in list_code:
            list_final_string.append(item)
        for arg in args:
            string = "import " + arg 
            list_final_string.append(string)

        for key, value in kwargs.items():
            key = key.replace('__', '.')
            
            list_final_string.append("from {} import {}".format(key, value))

        return('\n'.join(list_final_string))

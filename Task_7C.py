# Open Image file along with Image information,
# Cropping images,
# copying and pasting images,
# Create a Jupyter Notebook


# library to Create Jupyter Notebook
import nbformat as nbf

#Create Jupyter Notebook
nb = nbf.v4.new_notebook()

# MarkDown Cells
text = """\
# Working With Images
Open Image with Image Information."""

text1="""\
# Crop Image."""

text2="""\
# Copying And Pasting Images."""

# Code Cells
code = """\
import easygui
from PIL import Image
flower=Image.open('image_file.jpg')
print(flower.size)
print(flower.filename)
print(flower.format_description)
flower"""

code1="""\
cut_flower= flower.crop((120,100,200,200))
cut_flower"""

code2="""\
flower.paste(im=cut_flower,box=(300,0))
flower"""

nb['cells'] = [nbf.v4.new_markdown_cell(text),
               nbf.v4.new_code_cell(code),
               nbf.v4.new_markdown_cell(text1),
               nbf.v4.new_code_cell(code1),
               nbf.v4.new_markdown_cell(text2),
               nbf.v4.new_code_cell(code2)]
fname = 'Task_7C_book.ipynb'

with open(fname, 'w') as f:
    nbf.write(nb, f)
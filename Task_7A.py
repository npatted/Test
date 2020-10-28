# Create/Open XML file,
# Parse XML file,
# Modify XML file,
# Create a Jupyter Notebook



# Create Jupyter notebook using nbformat library
import nbformat as nbf

# Create Jupyter Notebook
nb = nbf.v4.new_notebook()

# Add Text input to Markdown Cell
text = """\
# Create XML File."""

text1 = """\
# Read XML File."""

text2 = """\
# Parse XML File."""

text3 = """\
# Modify XML File."""

# Add Code to Cells
code = """\
import xml.etree.ElementTree as xml

def createXML(filename):
   # Start with the root element
   root = xml.Element("Library")
   children1 = xml.Element("book")
   root.append(children1)
    
   Title = xml.SubElement(children1, "Title")
   Title.text = "Harry Potter"

   Author = xml.SubElement(children1, "Author")
   Author.text = "J K Rowling"

   Price = xml.SubElement(children1, "Price")
   Price.text = "2000"

   tree = xml.ElementTree(root)
   with open(filename, "wb") as fh:
        tree.write(fh)

if __name__ == "__main__":
   createXML("testXML.xml") """

code1 ="""\
with open('testXML.xml', 'r') as f: 
    data = f.read() 
data"""

code2 ="""\
import xml.etree.cElementTree as ET

def parseXML(file_name):
   # Parse XML with ElementTree
   tree = ET.ElementTree(file=file_name).getroot()
   

   
   for user in tree:
      for user_child in user:
         print("%s=%s" % (user_child.tag, user_child.text))

if __name__ == "__main__":
   parseXML("testXML.xml")"""

code3 ="""\
import xml.etree.ElementTree as ET

def updateET(filename):
   # Start with the root element
   tree = ET.ElementTree(file=filename)
   root = tree.getroot()

   for price in root.iter('Price'):
      price.text = '3000'

   tree = ET.ElementTree(root)
   with open("testXML.xml", "wb") as fh:
      tree.write(fh)

if __name__ == "__main__":
   updateET("testXML.xml")"""

code4 ="""\
with open('testXML.xml', 'r') as f: 
    data = f.read() 
data"""


# Create markdown and code Cell
nb['cells'] = [nbf.v4.new_markdown_cell(text),
               nbf.v4.new_code_cell(code),
               nbf.v4.new_markdown_cell(text1),
               nbf.v4.new_code_cell(code1),
               nbf.v4.new_markdown_cell(text2),
               nbf.v4.new_code_cell(code2),
               nbf.v4.new_markdown_cell(text3),
               nbf.v4.new_code_cell(code3),
               nbf.v4.new_code_cell(code4)]
fname = 'Task_7A_book.ipynb'

with open(fname, 'w') as f:
    nbf.write(nb, f)

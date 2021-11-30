import os

path = "People/Genesis 8 Male/Clothing/Basic Wear/Basic Wear Boxers.duf"
name = os.path.basename(path)
print(name)

name = name.replace('.duf', '')
print(name)

relFilePath = "People/Genesis 8 Male/Clothing/Basic Wear/Basic Wear Boxers.duf" #set relative fil path for render
fileName = os.path.basename(relFilePath)
fileName = fileName.replace('.duf', '')
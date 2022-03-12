import os


tempRenderFileName = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058WebAppV2/app/static/imageProperties/ImageProperties.txt"

renderFileName = os.path.basename(tempRenderFileName) 
renderFileName = renderFileName.replace('.txt','')

print(renderFileName)
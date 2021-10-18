import json
import os
import click


@click.option(help="Relative address for Daz3D Property file.")

def dazprops():
    """Read Daz3D property File"""
    
    path = click.prompt('Please specify a location for the Daz3D Properties File')
    path = os.path.realpath(path)

    return path 


    #dir_name = os.path.dirname(path)
    #print(path)
    #dazpropsf = open('path')
    #print(dazpropsf)


if __name__ == '__main__':
    file1 = dazprops()
    with open(file1) as newFile:
        Daz3DPropfile = json.load(newFile)
    print(Daz3DPropfile)

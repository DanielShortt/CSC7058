import json
import click


@click.command()
@click.option('--SciSceneDef', prompt="Please enter file location.",
                 help="The location of a scientific scene json file that will be used to create a Daz3D scene")
@click.option('--SceneID', prompt="Please enter a sceneID.",
                 help="This should be a uniqueID.")



def main(SciSceneDef,SceneID):

    '''
    Help Message -  This Program is intended to take in a JSON file containing a scientific representation of a 
    scene and output this into a Daz3D scene.
    '''

    #temp folder destination
    folderdestination = "D:\Software Masters\Year 3\TestFiles"

    #Opening scientific scene json file
    with open(f'{SciSceneDef}') as file1:
        SciDaz3DPropfile = json.load(file1)


    #Process of scene will happen here
    #temp processing of file
    SciDaz3DPropfileProcessed = SciDaz3DPropfile

    #out putting the Daz3d Scene JSON file
    Dazsceneloc = (f"{folderdestination}\{SceneID}.json")  
    with open (Dazsceneloc, 'w') as Daz3dV1:
        json.dump(SciDaz3DPropfileProcessed, Daz3dV1, indent=2)    


if __name__ == '__main__':
    main()
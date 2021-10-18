import json
import click

@click.command
@click.option('--dazscenespec1',prompt ="Please enter the location of cinema director output 1",
                 help= "The first cinema director output image after processing.")
@click.option('usersoftmeasurement', prompt="Please provide the user soft measurement file.",
                 help="The location of the softmeasurements provided by the user to alter the image.")

def main(dazscenespec1, usersoftmeasurement):
    '''
    This will take 5 inputs from the cinema director AI. The 5 scene specification outs. It will take the softmeasurements used to create 
    these scenes. It will then create files containing the soft measurements it thinks are needed to create these scenes.
    It will then compare the difference between the two files.
    '''
    click.echo("The critic will output it what it thinks the soft measurements should be for the provided cinema director output.")
    click.echo("The critic will then measure the different between different between it and the user output.")

    #Opening default daz3d property json file
    with open(f'{dazscenespec1}') as file1:
        Daz3DPropfile = json.load(file1)

    #opening the file with user selected soft measurements
    with open(f'{usersoftmeasurement}') as file2:
        UserSelectedSM = json.load(file2)

        

    #Critic will now create the soft measurements it thinks are needed to create this image and compare the difference
    
    
    
    #tempoutputlocation
    WriteLoc = "D:\Software Masters\Year 3\AICinematographer\Calibrated\TestFile"

    #outputting the soft measurements associated with the above daz3D file.
    #Naming convention up to be updated.
    softmout = (f"{WriteLoc}CriticSoftMeasurement.json")
    with open (softmout, 'w') as criticSM:
        json.dump(UserSelectedSM, criticSM, indent=2)


if __name__ == '__main__':
    main()
import json
import click

#setting up options for user input
@click.command()
@click.option('--dazscenespec', prompt ="Please enter Daz3D file location", help="File address for default Daz3D Property file.")
@click.option('--defaultsoftmeasurements', prompt ="Please enter Soft Measurement file location", help="Predefined Soft Measurements that reflect this stock image.")
@click.option('--usersoftmeasurements', prompt ="Please enter User Selected Soft Measurement file location", help="The Soft Measurement selections made by user.")
@click.option('--variationcount', prompt ="Please enter number of variations(Max 5)", help="The number of variation outputs.")
@click.option('--storage', prompt ="Please enter location of outputs.", help="The location the output files will be stored.")
@click.option('--resultuniqueid', prompt ="Please enter uniqueID for this file.", help="The UniqueID for this batch of output files.")

def main(dazscenespec, defaultsoftmeasurements, usersoftmeasurements, variationcount, storage, resultuniqueid):
    '''
    Help Message - This program is intended to take an image scene spec, user desired changes and output 5X updated variations.
    '''
    #Opening default daz3d property json file
    with open(f'{dazscenespec}') as file1:
        Daz3DPropfile = json.load(file1)

    #opening the softmeasurements that represent this image
    with open(f'{defaultsoftmeasurements}') as file2:
        DefaultSoftMeasurements = json.load(file2)

    #opening the file with user selected soft measurements
    with open(f'{usersoftmeasurements}') as file3:
        UserSelectedSM = json.load(file3)

    #storing output as variable
    WOutLoc = (f"{storage}")

    #out putting the daz3d property file
    dazpropsf = (f"{WOutLoc}Daz3DProps{resultuniqueid}.json")  
    with open (dazpropsf, 'w') as Daz3dV1:
        json.dump(Daz3DPropfile, Daz3dV1, indent=2)


    #outputting the soft measurements associated with the above daz3D file.
    softmout = (f"{WOutLoc}SoftM{resultuniqueid}.json")
    with open (softmout, 'w') as SoftMV1:
        json.dump(UserSelectedSM, SoftMV1, indent=2)

if __name__ == '__main__':
    main()
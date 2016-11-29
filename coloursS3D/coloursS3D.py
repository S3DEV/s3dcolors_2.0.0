'''------------------------------------------------------------------------------------------------
Program:    coloursS3D.py
Version:    1.1.1
Py Ver:     2.7
Purpose:    This is a utilities program to store commonly used colours and schemes for S3DEV
            products.

Dependents:

Comments:   Program to be stored in \Anaconda2\Libs\site-packages.

Use:        > import coloursS3D.coloursS3D as clrs
            > help(clrs)

---------------------------------------------------------------------------------------------------
UPDATE LOG:
Date        Programmer      Version     Update
07.08.16    J. Berendt      1.0.0       Copied and modified from colours.py (v2.0.0)
07.08.16    J. Berendt      1.1.0       Updated light grey text colours to 168, from 165.
29.11.16    J. Berendt      1.1.1       Non-functional changes:
                                        - cleaned up code
                                        Functional changes:
                                        - Added a dark text colour
------------------------------------------------------------------------------------------------'''

#--------------------------------------------------------------------------------------------------
#SET VERSION NUMBER
from _version import __version__ as __version__


#--------------------------------------------------------------------------------------------------
#FUNCTION TO RETURN ROLLS-ROYCE COLOUR SCHEME
def Colours(alpha=1.0):

    '''
    DESIGN:
    Function designed return colours from the 73rd Street Development colour scheme.

    The alpha parameter is optional.  Default = 1.0.

    SOURCE:
    This colour scheme was taken from the 73rd Street Development Standard Operating Procedures
    document: INPROCSP001 - General Standard Operating Procedures

    USE:
    > from coloursS3D.coloursS3D import Colours
    > cmap = Colours([alpha=0.5])
    '''

    #SET ALPHA LEVEL
    a = str(alpha)

    #CREATE COLOUR DICTIONARY
    colours = dict(
                clrs=dict
                    (
                    blue='rgba(0, 102, 225, ' + a + ')',
                    darkblue='rgba(31, 73, 125, ' + a + ')',
                    red='rgba(195, 0, 0, ' + a + ')'
                    ),
                grys=dict
                    (
                    light='rgba(240, 240, 240, ' + a + ')',
                    med='rgba(68, 68, 68, ' + a + ')',
                    dark='rgba(25, 25, 25, ' + a + ')'
                    ),
                txtgrys=dict
                    (
                    light='rgba(168, 168, 168, ' + a + ')',
                    med='rgba(128, 128, 128, ' + a + ')',
                    dark='rgba(75, 75, 75, ' + a + ')'
                    ))

    #RETURN DICTIONARY TO PROGRAM
    return colours
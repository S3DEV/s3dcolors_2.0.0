'''------------------------------------------------------------------------------------------------
Program:    s3dcolors
Version:    2.0.0
Py Ver:     2.7
Purpose:    This is a colour map utility program designed to store commonly used colours and
            schemes for S3DEV products.

Dependents: utils

Comments:

---------------------------------------------------------------------------------------------------
UPDATE LOG:
Date        Programmer      Version     Update
07.08.16    J. Berendt      1.0.0       Copied and modified from colours.py (v2.0.0)
07.08.16    J. Berendt      1.1.0       Updated light grey text colours to 168, from 165.
29.11.16    J. Berendt      1.1.1       Non-functional changes:
                                        - cleaned up code
                                        Functional changes:
                                        - Added a dark text colour
15.09.17    J. Berendt      2.0.0       Complete module overhaul, rename and class conversion.
                                        This version of s3dcolors was derived from EHM.colours.
                                        pylint (10/10)
------------------------------------------------------------------------------------------------'''

import utils.utils as u

#PURE CLASS MODULE.  NO METHODS NEEDED
#pylint: disable=too-few-public-methods
#ALLOW CLASS DOCSTRING
#pylint: disable=pointless-string-statement
#ENABLE LOCAL ACCESS TO _convert() FUNCTION / DISABLE OUTSIDE ACCESS
#pylint: disable=protected-access

#-----------------------------------------------------------------------
#PRIMARY CLASS
class CMaps(object):

    from _version import __version__

    '''
    PURPOSE:
    This class is designed to be the central source for S3DEV colour
    maps for Python visual applications.

    DESIGN:
    All colours used in this class have been taken from:
        INPROCSP001 - General Standard Operating Procedures.pdf

    The colours in each class are stored in rgba format.  However, some
    packages only accept colours in a hex format, e.g.: matplotlib.
    As such, each class contains a 'mode' parameter which can be passed
    as 'hex' (mode='hex') to convert the rgba string to a hex string -
    using the utils.rgb2hex() function.

    PREVIEW:
    To preview a colour map, adapt the example code below:

    > import utils.utils as u
    > from s3dcolors.s3dcolors import CMaps
    >
    > cmap_clrs = CMaps.Colours()
    > cmap = [v for k, v in vars(cmap_clrs).items()]
    > u._prev_plotly(cmap=cmap, cmap_name='Standard Colours')
    '''

    #-------------------------------------------------------------------
    #CLASS FOR STANDARD COLOURS
    class Colors(object):

        '''
        PURPOSE:
        The colours contained in the Colors class will typically be
        used for graphs and visuals created by Python applications.

        PARAMETERS:
        - alpha (default=1.0)
            The alpha (transparency) colour channel value.
            This value ranges from 0 to 1.0, where 0 is fully
            transparent.
        - mode (default='rgb')
            Type of colour string to return.  Note, the 'rgb' option
            includes an alpha parameter by default.
            Options: 'rgb', 'hex'
        - drop_alpha (default=False)
            When set to True, the alpha parameter is dropped from the
            hex string.  This parameter is only applied when
            mode='hex', and has no effect on 'rgb' strings.

        USE:
        > from s3dcolors.s3dcolors import CMaps
        > cmap_clrs = CMaps.Colors(alpha=0.75, mode='rgb')
        > clr_red = cmap_clrs.red
        '''

        def __init__(self, alpha=1.0, mode='rgb', drop_alpha=False):

            #CONVERT ALPHA VALUE TO STRING
            alpha = CMaps._convert(alpha)

            #PRIMARY
            self.blue       = 'rgba(000, 102, 225, %s)' % alpha
            self.darkblue   = 'rgba(031, 073, 125, %s)' % alpha
            self.red        = 'rgba(195, 000, 000, %s)' % alpha

            #TEST FOR HEX ARGUMENT >> CONVERT RGBA VALUE TO HEX
            if mode == 'hex':
                #PRIMARY
                self.blue       = u.rgb2hex(rgb_string=self.blue, drop_alpha=drop_alpha)
                self.darkblue   = u.rgb2hex(rgb_string=self.darkblue, drop_alpha=drop_alpha)
                self.red        = u.rgb2hex(rgb_string=self.red, drop_alpha=drop_alpha)


    #-------------------------------------------------------------------
    #CLASS FOR GREYS
    class Greys(object):

        '''
        DESIGN:
        The Greys class contains standard greys used by S3DEV.  The uses
        range from graph text (title, axis labels, ticks, etc.) to
        application backgrounds.

        PARAMETERS:
        - alpha (default=1.0)
            The alpha (transparency) colour channel value.
            This value ranges from 0 to 1.0, where 0 is fully
            transparent.
        - mode (default='rgb')
            Type of colour string to return.  Note, the 'rgb' option
            includes an alpha parameter by default.
            Options: 'rgb', 'hex'
        - drop_alpha (default=False)
            When set to True, the alpha parameter is dropped from the
            hex string.  This parameter is only applied when
            mode='hex', and has no effect on 'rgb' strings.

        USE:
        > from s3dcolors.s3dcolors import CMaps
        > cmap_gry = CMaps.Greys(mode='hex', drop_alpha=True)
        > clr_light_grey = cmap_gry.light
        '''

        def __init__(self, alpha=1.0, mode='rgb', drop_alpha=False):

            #CONVERT ALPHA VALUE TO STRING
            alpha = CMaps._convert(alpha)

            #COLOUR DEFINITIONS
            self.light_light    = 'rgba(240, 240, 240, %s)' % alpha
            self.light          = 'rgba(168, 168, 168, %s)' % alpha
            self.med_light      = 'rgba(128, 128, 128, %s)' % alpha
            self.med            = 'rgba(068, 068, 068, %s)' % alpha
            self.med_dark       = 'rgba(040, 040, 040, %s)' % alpha
            self.dark           = 'rgba(025, 025, 025, %s)' % alpha
            self.dark_dark      = 'rgba(010, 010, 010, %s)' % alpha

            #TEST FOR HEX ARGUMENT >> CONVERT RGBA VALUE TO HEX
            if mode == 'hex':
                #PRIMARY
                self.light_light    = u.rgb2hex(rgb_string=self.light_light, drop_alpha=drop_alpha)
                self.light          = u.rgb2hex(rgb_string=self.light, drop_alpha=drop_alpha)
                self.med_light      = u.rgb2hex(rgb_string=self.med_light, drop_alpha=drop_alpha)
                self.med            = u.rgb2hex(rgb_string=self.med, drop_alpha=drop_alpha)
                self.med_dark       = u.rgb2hex(rgb_string=self.med_dark, drop_alpha=drop_alpha)
                self.dark           = u.rgb2hex(rgb_string=self.dark, drop_alpha=drop_alpha)
                self.dark_dark      = u.rgb2hex(rgb_string=self.dark_dark, drop_alpha=drop_alpha)


    #-------------------------------------------------------------------
    #FUNCTION USED ACROSS THE CLASS TO CONVERT ALPHA VALUE TO A STRING
    @classmethod
    def _convert(cls, value):

        #RETURN ALPHA VALUE AS STRING
        return str(value) if not isinstance(value, str) else value

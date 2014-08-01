class PyColor:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DEFAULT = '\033[0m'

    @staticmethod
    def Disable():
        '''Abstracion to simply turn off color printing'''
        return PyColor.DEFAULT

    @staticmethod
    def getColorText(color, text):
        '''Return a colored text block

        @param color Color def from the static class variables
        @param text The text to print to print to the console

        '''
        return color + text + PyColor.DEFAULT

    @staticmethod
    def printColorText(color, text):
        '''Print a line of text in the color of your choosing

        @param color Color def from the static class variables
        @param text The text to print to the console

        '''
        print color + text + PyColor.DEFAULT
        return True
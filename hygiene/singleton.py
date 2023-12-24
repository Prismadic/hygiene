from hygiene.payload import boxing

class Singleton:
    """
    A utility class that provides access to the 'boxing' module from the 'payload' package.
    """

    @staticmethod
    def boxing():
        """
        Returns the 'boxing' module from the 'payload' package.
        
        :return: The 'boxing' module.
        """
        return boxing
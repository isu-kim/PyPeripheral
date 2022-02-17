"""
@project : PyPeripheralDemos
@author : Gooday2die
@date : 2022-02-16
@file : abstractDemo.py
"""

from abc import abstractmethod, ABCMeta


class AbstractDemo:
    """
    An abstract class for demo scripts.
    This class is meant to be inherited by child classes
    """
    @abstractmethod
    def __init__(self):
        self.thread = None
        self.is_running = False
        self.sdk_object = None

    @abstractmethod
    def run(self, **kwargs):
        """
        An abstract method for running this demo.
        This method will have main features of the demo script.
        :param kwargs: the kwargs of parameters
        :return: returns None
        """
        pass

    @abstractmethod
    def stop(self):
        """
        An abstract method for stopping this demo.
        This method will terminate the demo script and this object.
        :return:
        """
        pass

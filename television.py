# television baltimore anthem

class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    # define Television instance variables
    def __init__(self):
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    '''
    Toggle self.__status between True and False
    :self: all of the class variables and instance variables
    :return: returns self.__status as either boolean True or False 
    '''
    def power(self):
        if self.__status:
            self.__status: bool = False
        elif not self.__status:
            self.__status: bool = True
        return self.__status

    '''
    Toggle self.__muted value between True and False
    :self: all of the class variables and instance variables
    :return: returns self.__muted as either boolean True or False 
    '''
    def mute(self):
        if self.__muted:
            self.__muted: bool = False
        elif not self.__muted:
            self.__muted: bool = True
        return self.__muted

    '''
    Increments self.__channel up by one, wraps around MAX_CHANNEL value back to MIN_CHANNEL at top
    :self: all of the class variables and instance variables
    :return: returns self.__channel as an integer value
    '''
    def channel_up(self):
        if self.__channel == self.MAX_CHANNEL:
            self.__channel = self.MIN_CHANNEL
        else:
            self.__channel += 1
        return self.__channel

    '''
    Increments self.__channel down by one, wraps around MIN_CHANNEL back to MAX_CHANNEL at bottom
    :self: all of the class variables and instance variables
    :return: returns self.__channel as an integer value
    '''
    def channel_down(self):
        if self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL
        else:
            self.__channel -= 1
        return self.__channel

    ''''
    Increments self.__volume up by one, stops once if given MAX_VOLUME
    :self: all of the class variables and instance variables
    :return: returns self.__volume as an integer value
    '''
    def volume_up(self):
        if self.__volume != self.MAX_VOLUME:
            self.__volume += 1
        return self.__volume

    ''''
    Increments self.__volume down by one, stops once if at MIN_VOLUME
    :self: all of the class variables and instance variables
    :return: returns self.__volume as an integer value
    '''
    def volume_down(self):
        if self.__volume != self.MIN_VOLUME:
            self.__volume -= 1
        return self.__volume

    '''
    Gives viewer of program the current status of instance variables 
    :self: all of the class and instance variables
    :return: returns a formatted string showing the status of the variables
    '''
    def __str__(self):
        return f'Power = [{self.__status}], Channel =[{self.__channel}], Volume = [{self.__volume}]'

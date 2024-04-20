# television baltimore anthem

class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    # define Television instance variables
    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        if self.__status:
            self.__status = False
        elif not self.__status:
            self.__status = True
        return self.__status

    def mute(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            elif not self.__muted:
                self.__muted = True
            self.__volume = 0
        return self.__muted

    def channel_up(self):
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1
        return self.__channel

    def channel_down(self):
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1
        return self.__channel

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume += 1

            if self.__volume != self.MAX_VOLUME:
                self.__volume += 1
        return self.__volume

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = 2

            if self.__volume != self.MIN_VOLUME:
                self.__volume -= 1
        return self.__volume

    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

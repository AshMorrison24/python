class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.pre_mute = Television.MIN_VOLUME
    def power(self):
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False
    def mute(self):
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
                self.__volume = Television.MIN_VOLUME
            elif self.__muted == True:
                self.__muted = False
        else:
            self.__muted = self.__muted
    def channel_up(self):
        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
        else:
            self.__channel = self.__channel
    def channel_down(self):
        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
        else:
            self.__channel = self.__channel
    def volume_up(self):
        if self.__status == True:
            if self.__muted == False:
                if self.__volume == Television.MAX_VOLUME:
                    self.__volume = Television.MAX_VOLUME
                else:
                    self.__volume += 1
            elif self.__muted == True:
                self.__volume = self.pre_mute
                self.__volume += 1
                self.__muted = False
            self.pre_mute = self.__volume
        else:
            self.__volume = self.__volume
    def volume_down(self):
        if self.__status == True:
            if self.__muted == False:
                if self.__volume == Television.MIN_VOLUME:
                    self.__volume = Television.MIN_VOLUME
                else:
                    self.__volume -= 1
            elif self.__muted == True:
                self.__volume = self.pre_mute
                self.__volume -= 1
                self.__muted = False
            self.pre_mute = self.__volume
        else:
            self.__volume = self.__volume
    def __str__(self):
        return f"Power - {self.__status}, Channel - {self.__channel}, Volume - {self.__volume}"
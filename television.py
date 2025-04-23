class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3
    def __init__(self) -> None:
        """
        Function to initialize variables status, muted, volume, channel, and pre-mute.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        self.pre_mute: int = Television.MIN_VOLUME
    def power(self) -> None:
        """
        Function to turn tv on and off.
        """
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False
    def mute(self) -> None:
        """
        Function to mute and unmute tv.
        """
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
                self.__volume = Television.MIN_VOLUME
            elif self.__muted == True:
                self.__muted = False
        else:
            self.__muted = self.__muted
    def channel_up(self) -> None:
        """
        Function to turn tv channel up one.
        """
        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
        else:
            self.__channel = self.__channel
    def channel_down(self) -> None:
        """
        Function to turn tv channel down one.
        """
        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
        else:
            self.__channel = self.__channel
    def volume_up(self) -> None:
        """
        Function to turn tv volume up one.
        """
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
    def volume_down(self) -> None:
        """
        Function to turn tv volume down one.
        """
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
        """
        Function to print the tv status, channel, and volume.
        """
        return f"Power - {self.__status}, Channel - {self.__channel}, Volume - {self.__volume}"
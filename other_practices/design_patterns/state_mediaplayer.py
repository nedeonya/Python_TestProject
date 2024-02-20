from abc import ABC, abstractmethod


class PlayerState(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def pause(self):
        pass


class StoppedState(PlayerState):
    def play(self):
        print("Play media")
        return PlayingState()

    def pause(self):
        print("Can't pause, media is stopped")
        return self

    def stop(self):
        print("Already stopped")
        return self


class PlayingState(PlayerState):
    def play(self):
        print("Already playing")
        return self

    def pause(self):
        print("Pause media")
        return PausedState()

    def stop(self):
        print("Stop media")
        return StoppedState()


class PausedState(PlayerState):
    def play(self):
        print("Played media")
        return PlayingState()

    def pause(self):
        print("Already paused")
        return self

    def stop(self):
        print("Stop media")
        return StoppedState()


class Player:
    def __init__(self):
        self.state = StoppedState()

    def play(self):
        self.state = self.state.play()

    def pause(self):
        self.state = self.state.pause()

    def stop(self):
        self.state = self.state.stop()


#Testing
if __name__ == "__main__":
    player = Player()
    player.play()
    player.pause()
    player.stop()
    player.pause()
    player.play()

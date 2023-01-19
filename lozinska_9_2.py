import keyboard
from abc import ABCMeta, abstractmethod

class KeyboardListener(metaclass= ABCMeta):

    @abstractmethod
    def onKey(self, key : str):
        pass

class KeyboardSpy:

    def __init__(self):
        self.__listeners = set()

    def registerListener(self, listener):
        self.__listeners.add(listener)

    def main(self):
        flag = True
        while flag :
            try:
                key = keyboard.read_key()
                if keyboard.is_pressed("ctrl") and key == "q":  # To finish use "ctrl+q".
                    print('Finished!')
                    break

                for listener in self.__listeners:
                    listener.onKey(key)
                    
            except:
                break


class KeyLogger(KeyboardListener):
    def onKey(self, key):
        print('WAS PRESSED', key)

class KeyFileLogger(KeyboardListener):
    def __init__(self, filename):
        self.filename = filename
        self.key = []

    def onKey(self, key):
        with open(self.filename, 'w') as f:
            self.key.append(key)
            print(*self.key, file = f)

    def __str__(self):
        return 'FILLED IN!'


if __name__ == "__main__":
    keyboardSpy = KeyboardSpy()

    keyboardSpy.registerListener(KeyLogger())

    file = KeyFileLogger('input02.txt')
    keyboardSpy.registerListener(file)

    keyboardSpy.main()
    print(file)
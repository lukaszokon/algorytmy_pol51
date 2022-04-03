class Stack:
    class __Element:
        def __init__(self, value):
            self.value = value
            self.prev = None

    def __init__(self):
        self.__top = None

    def push(self, value):
        new_element = self.__Element(value)
        if not self.__top:
            self.__top = new_element
        else:
            new_element.prev = self.__top
            self.__top = new_element

    def pop(self):
        if self.__top:
            wierzcholek = self.__top
            value = wierzcholek.value
            self.__top = wierzcholek.prev
            return value
        else:
            return None

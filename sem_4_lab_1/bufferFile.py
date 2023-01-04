class BufferFile:

    def __init__(self, name: str, directory, max_size: int):
        if directory.count < directory.max_size:
            self.directory = directory
            self.directory.count = 1
            self.directory.list.append(self)
            self.max_size = max_size
            self.name = name
            self.contents = []
        else:
            print("This directory is already full")
            return

    def delete(self):
        print("Deleting " + self.name)
        index = self.directory.list.index(self)
        self.directory.list.pop(index)
        del self
        print("Deleted successfully")

    def move_buffer_file(self, location):
        if location.count < location.max_size:
            self.directory.count -= 1
            index = self.directory.list.index(self)
            self.directory.list.pop(index)
            self.directory = location
            self.directory.list.append(self)
            self.directory.count += 1
        else:
            print("Directory is already full")
            return

    def push_element(self, element):
        if len(self.contents) < self.max_size:
            self.contents.append(element)
        else:
            print("File already full")

    def consume_element(self, element):
        index = self.contents.index(element)
        self.contents.pop(index)

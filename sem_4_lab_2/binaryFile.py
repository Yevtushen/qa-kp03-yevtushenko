class BinaryFile:

    def __init__(self, name: str, directory, contents: str):
        if directory.count < directory.max_size:
            self.directory = directory
            self.directory.count = 1
            self.name = name
            self.contents = contents
            self.directory.list.append(self)
        else:
            print("This directory is already full")
            return

    def delete(self):
        print("Deleting " + self.name)
        index = self.directory.list.index(self)
        self.directory.list.pop(index)
        del self
        print("Deleted successfully")

    def move_binary_file(self, location):
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

    def read_file(self):
        print(self.contents)

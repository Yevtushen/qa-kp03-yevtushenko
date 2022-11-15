class BufferFile:

    def __init__(self, name: str, directory, max_size: int):
        if directory.count >= directory.max_size:
            print("This directory is already full")
            return
        self.directory = directory
        self.directory.count += 1
        self.directory.list.append(self)
        self.max_size = max_size
        self.name = name
        self.contents = []
        pass

    def __delete__(self, instance):
        print("Deleted successfully")

    def move_buffer_file(self, location):
        pass

    def push_element(self, element):
        if len(self.contents) < self.max_size:
            self.contents.append(element)
        else:
            print("File already full")

    def consume_element(self):
        self.contents.pop()

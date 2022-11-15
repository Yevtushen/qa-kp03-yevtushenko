class LogTextFile:

    def __init__(self, name: str, directory, contents: str):
        if directory.count < directory.max_size:
            self.directory = directory
            self.directory.count += 1
            self.name = name
            self.contents = contents
            self.directory.list.append(self)
        else:
            print("This directory is already full")
            return

    def __delete__(self, instance):
        print("Deleted successfully")

    def move_log_file(self, location):
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
        return self.contents

    def append_line(self, line: str):
        self.contents += '\n' + line

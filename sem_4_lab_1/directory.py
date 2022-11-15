class Directory:

    def __init__(self, name: str, parent_directory, max_size: int):
        if parent_directory.count < parent_directory.max_size:
            parent_directory.count += 1
            parent_directory.list.append(self)
            self.name = name
            self.parent_directory = parent_directory
            self.max_size = max_size
            self.count = 0
            self.list = []
        else:
            print("This directory is already full")
            return


    def __delete__(self, instance):
        print("Deleted successfully")

    def list_elements(self):
        resulting_list = 'In ' + self.name + ': '
        for element in self.list:
            resulting_list += element.name + '; '
        print(resulting_list)

    def move_directory(self, location):
        if location.count < location.max_size + self.count + 1:
            self.parent_directory.count_elems -= self.count + 1
            index = self.parent_directory.list.index(self)
            self.parent_directory.list.pop(index)
            self.parent_directory = location
            self.parent_directory.list.append(self)
            self.parent_directory.count_elems += 1
        else:
            print("Directory is already full")
            return

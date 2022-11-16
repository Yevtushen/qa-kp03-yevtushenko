#print("Hello world")
from directory import Directory
from binaryFile import BinaryFile
from logTextFile import LogTextFile
from bufferFile import BufferFile

root = Directory('root', None, 20)
directory1 = Directory('dir1', root, 15)
directory2 = Directory('dir2', root, 15)
directory1_1 = Directory('dir1_1', directory1, 3)
bin_f1 = BinaryFile('binF1', directory1, '0101')
bin_f2 = BinaryFile('binF2', directory1_1, '10')
log_f1 = LogTextFile('logF1', directory2, 'some text')
log_f2 = LogTextFile('logF2', directory2, 'another text')
buf_f1 = BufferFile('bufF1', directory1, 30)
buf_f2 = BufferFile('bufF2', root, 40)

root.list_elements()
directory1.list_elements()
directory1_1.list_elements()
directory2.list_elements()
print('----------------------')
directory2.move_directory(directory1)
buf_f1.delete()
log_f1.move_log_file(directory1)
directory1.list_elements()
print('----------------------')
log_f2.append_line('and more another text')
log_f2.read_file()

class DirectoryIter:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index += 1
            return self.wrapped[self.index - 1]
        else:
            raise StopIteration


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f'{self.name} \t -> \t {self.size} bytes'


class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []

    def __str__(self):
        result = f'{self.name} \n\t'
        result += '\n\t'.join(map(str, self.files))
        return result

    def __add__(self, other):
        if not isinstance(other, File):
            return NotImplemented
        self.files.append(other)

    # sequences protocol
    def __getitem__(self, index):
        if not isinstance(index, (slice, int)):
            raise TypeError
        return self.files[index]

    def __len__(self):
        return len(self.files)

    # iteration protocol
    def __iter__(self):
        return DirectoryIter(self.files)


# test

file_1 = File('test1.txt', 120)
file_2 = File('test2.txt', 102)
file_3 = File('test3.txt', 145)

dir_1 = Directory('My_dir')
dir_1 + file_1
dir_1 + file_2
dir_1 + file_3

for i in dir_1:
    print(i)

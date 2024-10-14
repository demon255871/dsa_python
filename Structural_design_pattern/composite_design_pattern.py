"""
The Composite Pattern is a structural design pattern used to treat individual objects and compositions of objects uniformly. This pattern is useful when you want to represent part-whole hierarchies, like a tree structure, where both composite objects (which contain other objects) and leaf objects (which do not contain other objects) need to be treated the same way.
Example: File System Hierarchy

Let's take an example where we want to represent a file system consisting of files and directories. Both files and directories share some common operations like show() (to display their contents), but a directory can contain multiple files or subdirectories.

Explanation:

    FileSystemComponent (Component):
        This is the abstract base class that defines a common interface for both Leaf (File) and Composite (Directory) objects. It has an abstract method show(), which must be implemented by all subclasses.

    File (Leaf):
        The File class represents leaf objects. A leaf has no children and implements the show() method to return the file’s name.

    Directory (Composite):
        The Directory class represents composite objects, which can contain children (other files or directories). It has methods like add() and remove() to manage its children, and it implements the show() method to display its name along with its children's names recursively.

    Client Code:
        The client_code() function takes any FileSystemComponent object and prints its contents using the show() method. The client code doesn't need to know whether it's working with a file or a directory; it treats both uniformly.
"""
from abc import ABC, abstractmethod

# Component: Abstract base class
class FileSystemComponent(ABC):
    @abstractmethod
    def show(self):
        pass

# Leaf: File class (cannot contain other components)
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show(self):
        return self.name

# Composite: Directory class (can contain other files or directories)
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def show(self):
        results = [f"Directory: {self.name}"]
        for child in self.children:
            results.append(f"  {child.show()}")
        return "\n".join(results)

# Client Code
def client_code(component: FileSystemComponent):
    print(component.show())

# Usage
file1 = File("file1.txt")
file2 = File("file2.txt")
subdir = Directory("subdir")
subdir.add(file1)

root_dir = Directory("root")
root_dir.add(subdir)
root_dir.add(file2)

# Show the structure
client_code(root_dir)

# Outputs:
# Directory: root
#   Directory: subdir
#     file1.txt
#   file2.txt

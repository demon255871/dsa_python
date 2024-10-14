"""
GPT

The Template Method Pattern is a behavioral design pattern that defines the skeleton of an algorithm in a method, allowing subclasses to override certain steps of the algorithm without changing its structure. This promotes code reuse by having a common algorithm in a base class while allowing specific steps to be implemented differently by subclasses.
Example: Data Processing Template

In this example, we’ll create a template for a data processing pipeline. Different types of data (e.g., CSV, JSON) will be processed by following a general flow, but certain steps (like reading the data and processing it) will vary depending on the data format. The template method in the base class will define the overall structure, while the concrete subclasses will provide the specific implementations.

Explanation:

    DataProcessor (Template Class):
        This is the abstract class that defines the template method process(). The process() method provides a skeleton for the data processing workflow: it consists of three steps: read_data(), process_data(), and save_data().
        The steps read_data() and process_data() are declared as abstract methods, meaning the concrete subclasses must implement them.
        The save_data() method is implemented in the base class and is the same for all subclasses.

    Concrete Subclasses:
        CSVDataProcessor: Implements the read_data() and process_data() methods for reading and processing CSV files.
        JSONDataProcessor: Implements the read_data() and process_data() methods for reading and processing JSON files.
        Both classes inherit the save_data() method from the base class, which saves the processed data in a generic way (e.g., to a file).

    Client Code:
        The client uses the DataProcessor interface to invoke the process() method. The exact behavior (whether CSV or JSON data is processed) is determined by which concrete subclass is passed to the client code.
"""


from abc import ABC, abstractmethod

# Abstract Class: DataProcessor (Template)
class DataProcessor(ABC):
    # Template Method
    def process(self):
        self.read_data()
        self.process_data()
        self.save_data()

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def process_data(self):
        pass

    def save_data(self):
        print("Saving data to a file.")

# Concrete Class 1: CSV Data Processor
class CSVDataProcessor(DataProcessor):
    def read_data(self):
        print("Reading data from a CSV file.")

    def process_data(self):
        print("Processing CSV data.")

# Concrete Class 2: JSON Data Processor
class JSONDataProcessor(DataProcessor):
    def read_data(self):
        print("Reading data from a JSON file.")

    def process_data(self):
        print("Processing JSON data.")

# Client Code
def client_code(data_processor: DataProcessor):
    data_processor.process()

# Usage
print("Processing CSV data:")
csv_processor = CSVDataProcessor()
client_code(csv_processor)

print("\nProcessing JSON data:")
json_processor = JSONDataProcessor()
client_code(json_processor)

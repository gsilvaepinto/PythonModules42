import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self):
        self.data = []
        self.index = -1

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        data = self.data.pop(0)
        self.index += 1
        return self.index, data


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            result = True
        elif isinstance(data, list) and all(
            isinstance(i, (int, float)) for i in data
        ):
            result = True
        else:
            result = False
        print(f"Trying to validate input '{data}': {result}")
        return result

    def ingest(self, data: typing.Union[int, float, list]) -> None:
        if isinstance(data, (int, float)):
            self.data.append(str(data))
        elif isinstance(data, list) and all(
            isinstance(i, (int, float)) for i in data
        ):
            for value in data:
                self.data.append(str(value))
        else:
            raise TypeError("Improper numeric data")


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            result = True
        elif isinstance(data, list) and all(isinstance(i, str) for i in data):
            result = True
        else:
            result = False
        print(f"Trying to validate input '{data}':", result)
        return result

    def ingest(self, data: typing.Union[str, list]) -> None:
        if isinstance(data, str):
            self.data.append(data)
        elif isinstance(data, list) and all(isinstance(i, str) for i in data):
            for value in data:
                self.data.append(value)
        else:
            raise TypeError("Improper string data")


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            result = True
        elif isinstance(data, list) and all(
            isinstance(i, dict) for i in data
        ):
            result = True
        else:
            result = False
        print(f"Trying to validate input '{data}':", result)
        return result

    def ingest(self, data: typing.Union[dict, list]) -> None:
        if isinstance(data, dict):
            self.data.append(data)
        elif isinstance(data, list) and all(
            isinstance(i, dict) and all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in i.items()
            ) for i in data
        ):
            for i in data:
                self.data.append(f"{i['log_level']}: {i['log_message']}")
        else:
            raise TypeError("Improper log data")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    processor = NumericProcessor()
    processor.validate(42)
    processor.validate('Hello')
    try:
        print("Test invalid ingestion of string 'foo' "
              "without prior validation:")
        processor.ingest('foo')  # type: ignore
    except TypeError as e:
        print("Got exception:", e)
    data = [1, 2, 3, 4, 5]
    processor.ingest(data)
    print(f"Processing data: {data}")
    print("Extracting 3 values...")
    for item in range(3):
        index, value = processor.output()
        print(f"Numeric value {index}: {value}")

    print("\nTesting Text Processor...")
    textprocessor = TextProcessor()
    textprocessor.validate(42)
    values = ['Hello', 'Nexus', 'World']
    textprocessor.ingest(values)
    print(f"Processing data: {values}")
    print("Extracting 1 value...")
    for text in range(1):
        index, value = textprocessor.output()
        print(f"Text value {index}: {value}")

    print("\nTesting Log Processor...")
    logprocessor = LogProcessor()
    logprocessor.validate('Hello')
    logs = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    logprocessor.ingest(logs)
    print("Processing data:", logs)
    print("Extracting 2 values...")
    for item in range(2):
        index, value = logprocessor.output()
        print(f"Log entry {index}: {value}")

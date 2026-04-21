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


class DataStream:
    def __init__(self):
        self.processors: list[DataProcessor] = []
        self.total: dict[str, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)
        self.total[type(proc).__name__] = 0

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            handled = False
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    if isinstance(element, list):
                        self.total[type(proc).__name__] += len(element)
                    else:
                        self.total[type(proc).__name__] += 1
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - Can't process "
                      f"element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            name = type(proc).__name__
            print(f"{name}: total {self.total[name]} items processed, "
                  f"remaining {len(proc.data)} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    numeric = NumericProcessor()
    ds.register_processor(numeric)

    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! '
                                                 'Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]

    print("\nRegistering Numeric Processor")

    print("\nSend first batch of data on stream:", batch)
    ds.process_stream(batch)
    ds.print_processors_stats()

    text = TextProcessor()
    log = LogProcessor()
    print("\nRegistering other data processors")
    print("Print the same batch again")
    ds.register_processor(text)
    ds.register_processor(log)
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("\nConsume some elements from the "
          "data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    log.output()
    ds.print_processors_stats()

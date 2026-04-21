import typing
from typing import Protocol
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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            data = []
            for _ in range(nb):
                if not proc.data:
                    break
                data.append(proc.output())
            plugin.process_output(data)


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [element[1] for element in data]
        print("CSV Output:")
        print(",".join(values))


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = [f'"item_{element[0]}": "{element[1]}"' for element in data]
        print("JSON Output: ")
        print("{" + ", ".join(items) + "}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...\n")

    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Processors\n")

    batch = ['Hello world', [3.14, -1, 2.71],
             [{'log_level': 'WARNING',
               'log_message': 'Telnet access! Use ssh instead'},
              {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
             42, ['Hi', 'five']]

    print(f"Send first batch of data stream: {batch}\n")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    ds.register_processor(numeric)
    ds.register_processor(text)
    ds.register_processor(log)
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, CSVPlugin())

    print("")
    ds.print_processors_stats()

    second = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
              [{'log_level': 'ERROR', 'log_message': '500 server crash'},
               {'log_level': 'NOTICE', 'log_message':
                   'Certificate expires in 10 days'}],
              [32, 42, 64, 84, 128, 168], 'World hello']

    print(f"\nSend another batch of data: {batch}\n")
    ds.process_stream(second)
    ds.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, JSONPlugin())

    print("")
    ds.print_processors_stats()

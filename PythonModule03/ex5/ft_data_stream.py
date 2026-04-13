import typing
import random

ALL_PLAYERS: list[str] = ['bob', 'alice', 'dylan', 'charlie']
ALL_ACTIONS: list[str] = ['run', 'eat', 'sleep', 'grab', 'run', 'move']


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield random.choice(ALL_PLAYERS), random.choice(ALL_ACTIONS)


if __name__ == '__main__':
    print("=== Game Data Stream Processor ===")
    data: typing.Generator[tuple[str, str], None, None] = gen_event()
    for i in range(1000):
        name, action = next(data)
        print(f"Event {i}: Player {name} did action {action}")
    events: list[tuple[str, str]] = []
    for i in range(10):
        name, action = next(data)
        events.append((name, action))
    print(f"Built list of 10 events: {events}")
    for i in range(10):
        value = random.choice(events)
        print(f"Got event from list: {value}")
        events.remove(value)
        print(f"Remains in list: {events}")

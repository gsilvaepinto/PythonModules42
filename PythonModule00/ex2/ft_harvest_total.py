def ft_harvest_total() -> None:
    total = 0
    for day in range(1, 4):
        total += int(input(f"Day {day} harvest: "))
    print(f"Total harvest: {total}")

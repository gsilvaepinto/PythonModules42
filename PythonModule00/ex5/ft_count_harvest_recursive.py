def ft_count_harvest_recursive() -> None:
    total_days = int(input("Days until harvest: "))

    def print_days(num) -> None:
        if num > total_days:
            return
        print(f"Day {num}")
        print_days(num + 1)

    print_days(1)
    print("Harvest time!")

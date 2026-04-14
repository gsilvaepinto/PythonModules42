def secure_archive(filename: str, action: str = 'r',
                   content: str = '') -> tuple[bool, str]:
    try:
        with open(filename, action) as file:
            if action == 'r':
                return True, file.read()
            elif action == 'w':
                file.write(content)
                return True, 'Content successfully written to file'
            else:
                return False, 'INVALID ACTION'
    except FileNotFoundError as e:
        return False, str(e)
    except PermissionError as e:
        return False, str(e)


if __name__ == '__main__':
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file'))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('example'))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive('another'))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive('rrr', 'w', "this is an example file\n"))

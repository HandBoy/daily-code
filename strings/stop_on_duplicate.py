class DuplicateError(Exception):
    pass


def stop_on_duplicate(text):
    last = None

    try:
        for letter in text:
            if letter == last:
                raise DuplicateError()
            last = letter

    except DuplicateError:
        return True

    return False


if __name__ == "__main__":
    assert stop_on_duplicate("shep") is False
    assert stop_on_duplicate("sheep") is True

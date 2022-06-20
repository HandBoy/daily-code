def segment(x, space):
    # Write your code here
    min_values = []

    for index, value in enumerate(space):
        idx = index + 1
        end = index + x
        min_value = space[index]
        while idx < end:
            if space[idx] < min_value:
                min_value = space[idx]
            idx += 1

        min_values.append(min_value)

        if index + x >= len(space):
            break
    max_value = sorted(min_values)[:-1]
    return max_value



    return max_value


if __name__ == "__main__":
    assert 3 == segment(1, [1, 2, 3, 1, 2] )
    assert 4 == segment(3, [2, 5, 4, 6, 8])
    assert 1 == segment(2, [1, 1, 1])

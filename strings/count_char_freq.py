
def count_freq_char(list_of_char):
    """
    {
        "h": 1,
        "e": 1,
        "l": 2,
    }

    []: 
    []:  []->[]->[]
    """
    count_dict = {}
    for letter in list_of_char: 
        if letter.lower() in count_dict:
            count_dict[letter.lower()] += 1
            continue
        
        count_dict[letter.lower()] = 1

    return count_dict


if __name__ == "__main__":
    print(count_freq_char('Hello Hand') )
    print(count_freq_char('wwwaaf') )
    print(count_freq_char('Wwwaaf') )
    print(count_freq_char('aaaaaaa') )

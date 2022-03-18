def get_words_from_phone_number(phone_number):
    """
    Args:
     phone_number(str)
    Returns:
     list_str
    """
    # Write your code here.


    result = []

    new_phone_number = phone_number.replace("1", "").replace("0", "")
    if len(new_phone_number) == 0:
        return ["-1"]
    permute_phone_numbers(0, [], new_phone_number, result)

    return result

def permute_phone_numbers(i, slate, phone_number, result):
    hashNumbers = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": [
    "m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
    if i == len(phone_number):
        if len(slate) > 0:
            result.append("".join(slate))
        return

    for letter in hashNumbers[phone_number[i]]:
        slate.append(letter)
        permute_phone_numbers(i + 1, slate, phone_number, result)
        slate.pop()

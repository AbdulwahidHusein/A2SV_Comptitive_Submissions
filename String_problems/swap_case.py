def swap_case(s):
    def toggle(w):
        if w.isupper():
            return w.lower()
        return w.upper()
        
    swapped = ''
    for letter in s:
        if letter.isalpha():
            swapped += toggle(letter)
        else:
            swapped += letter
    return swapped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
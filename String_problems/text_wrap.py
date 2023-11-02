import textwrap

def wrap(string, max_width):
    s = ''
    start , end = 0, max_width
    while end <= len(string):
        s += string[start:end] + '\n'
        start = end
        end += max_width
    if start < len(string):
        s += string[start:]
        
    return s
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
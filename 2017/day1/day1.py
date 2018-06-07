def solution1(input_string):
    circular_input = input_string + input_string[0]

    answer = 0
    last = ''
    for char in circular_input:
        if char == last:
            answer += int(last)
        last = char
    
    return answer

def solutionN(input_string, skip=None):
    length = len(input_string) 
    if not skip:
        skip = length/2

    answer = 0
    for i in tuple(range(length)):
        next_i = int((i+skip)%length)
        if input_string[i] == input_string[next_i]:
            answer += int(input_string[i])
    return answer

def main(input_file):
    with open(input_file) as infile:
        input_string = infile.read().strip()

    print('Solution1:', solutionN(input_string, 1))
    print('SolutionN:', solutionN(input_string))

if __name__ == '__main__':
    import sys

    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'

    main(input_file)

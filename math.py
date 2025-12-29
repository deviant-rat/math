def get_numbers():
    user_list = input("please, input your numbers (pattern: 1 2 9)\n >")
    try:
        numbers = list(map(int, user_list.split()))
        return numbers
    except ValueError:
        print("Please, enter numbers")
        return None
    
def count_even():
    numbers = get_numbers()
    if numbers == None: return
    count = 0
    for item in numbers:
        if item % 2 == 0: 
            count+=1
    print(f"The ammount of even numbers is {count}")

def find_max():
    numbers = get_numbers()
    if numbers is None: return
    max = numbers[0]
    for item in numbers:
        if max < item: max = item
    print(f"The biggest number is {max}")

def filter_positive():
    numbers = get_numbers()
    if numbers is None: return
    pos_numbers = []
    for item in numbers:
        if item > 0: pos_numbers.append(item)
    print(pos_numbers)

def check_palindrome():
    line = input("Please, input you line \n >").strip().lower()
    line = line.replace(" ", "")
    size = len(line)
    len_os_line = int(size/2)
    for i in range(0, len_os_line):
        if line[i] != line[size-i-1]:
            return False
    return True


def main():
    while True:
        user_command = input("Please enter command\n > ").strip().lower()
        if user_command == "even":
            count_even()
        if user_command == "max":
            find_max()
        if user_command == "positive":
            filter_positive()
        if user_command == "pali":
            print(check_palindrome())
        if user_command == "exit":
            break

    

if __name__ == "__main__":
    main()
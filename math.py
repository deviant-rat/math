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

def check_list(my_list, my_word):
    for item in my_list:
        if item["text"] == my_word:
            item["count"] = item["count"] + 1
            return
    new_item = {"text": my_word, "count": 1}
    my_list.append(new_item)


def word_count():
    line = input("Please, input you line \n >").strip().lower()
    list_of_words = line.split()
    size = len(list_of_words)
    first = {"text": list_of_words[0], "count": 1}
    dict_of_words = []
    dict_of_words.append(first)
    for i in range(1, size):
        check_list(dict_of_words, list_of_words[i])
    print(dict_of_words)

def add_uniq(my_list, my_word):
    for item in my_list:
        if item == my_word:
            return
    my_list.append(my_word)


def find_uniq():
    line = input("Please, input you line \n >").strip().lower()
    list_of_words = line.split()
    size = len(list_of_words)
    uniq_list = [list_of_words[0]]
    for i in range(1, size):
        add_uniq(uniq_list, list_of_words[i])
    print(uniq_list)

def find_max():
    numbers = get_numbers()
    if numbers is None: return
    max = numbers[0]
    for item in numbers:
        if max < item: max = item
    print(f"The biggest number is {max}")
 

def second_max():
    numbers = get_numbers()
    if numbers == None: return
    size = len(numbers)
    for n in range(0,2):
        for i in range(1, size):
            if numbers[i]>numbers[n]: 
                temp = numbers[n]
                numbers[n] = numbers[i]
                numbers[i] = temp
    print (numbers[1])



def intersection():
    line = input("Please, input first list \n >").strip().lower()
    first_list = line.split()
    line = input("Please, input second list \n >").strip().lower()
    second_list = line.split()
    third_list = []
    for item in first_list:
        for item_two in second_list:
            if item == item_two:
                add_uniq(third_list, item)
    print(third_list)




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
        if user_command == "count":
            word_count()
        if user_command == "uniq":
            find_uniq()
        if user_command == "2max":
            second_max()
        if user_command == "overlap":
            intersection()
        if user_command == "exit":
            break

    

if __name__ == "__main__":
    main()
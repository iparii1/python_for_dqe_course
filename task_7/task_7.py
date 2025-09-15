import csv


def word_count(filepath: str) -> dict:
    with open(filepath, 'r') as f:
        text = f.read()
        words = text.lower().split()
        word_list = {}
        for word in words:
            if word.isalpha():
                if word not in word_list:
                    word_list[word] = 1
                else:
                    word_list[word] += 1
    return word_list


def letter_count(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
        lower_list = {}
        upper_list = {}

        for letter in text:
            if letter.isalpha():
                if letter.isupper():
                    if letter not in upper_list.keys():
                        upper_list[letter] = 1
                    else:
                        upper_list[letter] += 1
                else:
                    if letter not in lower_list.keys():
                        lower_list[letter] = 1
                    else:
                        lower_list[letter] += 1
    return upper_list, lower_list


def calculate_letters(upper_dct, lower_dct):
    result = {}
    for i in lower_dct:
        result[i] = upper_dct[i.upper()] + lower_dct[i] if i.upper() in upper_dct else lower_dct[i]
    return result


def letter_result(all_list, upper_list):
    result = []
    for letter, total_count in all_list.items():
        upper_count = upper_list.get(letter.upper(), 0)
        percentage = round((upper_list.get(letter.upper(), 0) / all_list[letter] * 100), 2) if total_count else 0
        line = f'{letter}, {total_count}, {upper_count}, {percentage}'
        result.append(line)
    return result


def write_to_csv_letters(letter_counts):
    field_names = ['letter', 'total_count', 'upper_count', 'percentage']

    with open('lettercount.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()

        for line in letter_counts:
            letter, total, upper, percent = line.split(', ')
            writer.writerow({
                'letter': letter,
                'total_count': total,
                'upper_count': upper,
                'percentage': percent
             })


def write_to_csv_words(word_dict):
    with open('wordcount.csv', 'w', newline='') as f:
        field_names = ['word', 'count']
        csv_writer = csv.DictWriter(f, fieldnames=field_names)
        csv_writer.writeheader()
        for word, count in word_dict.items():
            csv_writer.writerow({'word': word, 'count': count})


def main():
    file = r'C:/Users/Iryna_Parii/PycharmProjects/dqe_task1/pythonProject/task_4/output_file.txt'
    word_result = word_count(file)
    upper, lower = letter_count(file)
    total = calculate_letters(upper, lower)
    letters = letter_result(total, upper)
    write_to_csv_words(word_result)
    write_to_csv_letters(letters)


if __name__ == '__main__':
    main()

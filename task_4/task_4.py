import os
from datetime import datetime, date
from task_3.task_3 import normalize_text


class NewsFeed:
    def __init__(self, text: str):
        self.text = normalize_text(text)
        self.current_date = datetime.now()

    def get_result(self) -> str:
        pass

    def save_result(self) -> None:
        with open('output_file.txt', 'a') as my_file:
            my_file.write(self.get_result())


class News(NewsFeed):
    def __init__(self, text: str, city: str):
        super().__init__(text)
        self.city = normalize_text(city)
        self.date_published = self.current_date.strftime('%d/%m/%Y %H:%M')

    def get_result(self) -> str:
        return f'\n\nNews ----------\n{self.text}\n{self.city}, {self.date_published}'


class PrivateAd(NewsFeed):
    def __init__(self, text: str, exp_date: str):
        super().__init__(text)
        try:
            self.exp_date = datetime.strptime(exp_date.strip(), '%d/%m/%Y').date()
        except ValueError:
            print('Invalid date format.')

    def get_days_left(self) -> int:
        days_left = (self.exp_date - self.current_date.date()).days
        return max(days_left, 0)

    def get_result(self) -> str:
        formatted_date = self.exp_date.strftime('%d/%m/%Y')
        days_left = self.get_days_left()
        return f'\n\nPrivate Ad ----------\n{self.text}\nActual until: {formatted_date}, {days_left} days left'


class FileProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_file(self) -> list[str]:
        with open(self.file_path, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
        return lines

    def parse_records(self, lines: list[str]) -> list[NewsFeed]:
        parsed_records = []
        for line in lines:
            record_type, text, field = line.split('|')
            record_type = record_type.strip().lower()

            if record_type == 'news':
                parsed_records.append(News(text.strip(), field.strip()))
            elif record_type == 'private ad':
                parsed_records.append(PrivateAd(text.strip(), field.strip()))
            else:
                continue
        return parsed_records

    def process_file(self):
        lines = self.read_file()
        records = self.parse_records(lines)
        for record in records:
            record.save_result()
        os.remove(self.file_path)
        print(f"Processed file '{self.file_path}' and removed it.")


def select_input_file(default_folder: str = 'input_files', default_file: str = 'records.txt') -> str:
    print("Do you want to use the default file? (Default: input_files/records.txt)")
    user_input = input("Enter 'yes' for default or 'no' for a custom file: ").strip().lower()

    if user_input == 'yes':
        folder_path = os.path.join(os.getcwd(), default_folder)
        file_path = os.path.join(folder_path, default_file)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        if not os.path.exists(file_path):
            open(file_path, 'w').close()
        return file_path
    elif user_input == 'no':
        custom_path = input("Please provide the full path to the input file: ").strip()
        return custom_path
    else:
        exit()


def main():
    print("Welcome to the News Feed Tool!")
    print("1 - Process records from a file")
    print("2 - Manually input a record")

    choice = input("Please select option 1 or 2: ").strip()

    if choice == '1':
        default_folder = 'input_files'
        default_file = 'records.txt'
        file_path = select_input_file(default_folder, default_file)
        processor = FileProcessor(file_path)
        processor.process_file()
    elif choice == '2':
        print("1 - News\n2 - Private Ad")
        record_type = input("Select the type of record to add - 1 for News, 2 for Private Ad): ").strip()
        if record_type == '1':
            text = input("Enter the news text: ")
            city = input("Enter the city: ")
            record = News(text, city)
            record.save_result()
        elif record_type == '2':
            text = input("Enter the ad text: ")
            expiration_date = input("Enter the expiration date (DD/MM/YYYY): ")
            record = PrivateAd(text, expiration_date)
            record.save_result()
        else:
            print("Invalid record type.")
    else:
        print("Invalid option. Exiting.")


if __name__ == "__main__":
    main()

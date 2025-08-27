from datetime import datetime

try:
    input_prompt = ('1 - News\n'
                    '2 - Private Ad\n'
                    'Please enter the data type number to proceed: ')
    select_type = int(input(input_prompt).strip())
except ValueError:
    select_type = 0


class NewsFeed:
    def __init__(self):
        self.text = input('Please, enter your text: ')

    def get_result(self) -> str:
        pass

    def save_result(self) -> None:
        pass


class News(NewsFeed):
    def __init__(self):
        super().__init__()
        self.city = input('Enter the city: ')
        self.date_published = datetime.now().strftime('%d/%m/%Y %H:%M')

    def get_result(self) -> str:
        return f'\n\nNews ----------\n{self.text}\n{self.city}, {self.date_published}'

    def save_result(self) -> None:
        with open('output_file.txt', 'a') as my_file:
            my_file.write(self.get_result())


class PrivateAd(NewsFeed):
    def __init__(self):
        super().__init__()
        self.expiration_date = self.get_expiration_date()

    def get_expiration_date(self) -> datetime.date:
        while True:
            date_string = input('Enter expiration date in a format DD/MM/YYYY: ')
            try:
                expiration_date = datetime.strptime(date_string, '%d/%m/%Y').date()
                return expiration_date
            except ValueError:
                print('Invalid date format. Please enter correct expiration date.')

    def get_days_left(self) -> int:
        current_date = datetime.now().date()
        days_left = (self.expiration_date - current_date).days
        return max(days_left, 0)

    def get_result(self) -> str:
        formatted_date = self.expiration_date.strftime('%d/%m/%Y')
        days_left = self.get_days_left()
        return f'\n\nPrivate Ad ----------\n{self.text}\nActual until: {formatted_date}, {days_left} days left'

    def save_result(self) -> None:
        with open('output_file.txt', 'a') as my_file:
            my_file.write(self.get_result())


if select_type == 1:
    obj = News()
elif select_type == 2:
    obj = PrivateAd()

else:
    obj = None
    print('Invalid type.')

if obj:
    obj.save_result()

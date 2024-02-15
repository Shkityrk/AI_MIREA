import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import yfinance as yf
import warnings
import pandas as pd

confirm_data=False
while confirm_data==False:
    start_date = str(input("Введите начальный день в формате ГГГГ-ММ-ДД: "))
    end_date = str(input("Введите конечный день в формате ГГГГ-ММ-ДД: "))

    if len(start_date)!=10 or len(end_date)!=10:
        print("Ошибка. Введите снова")
    else:
        confirm_data=True


warnings.filterwarnings("ignore")  # игнорируем исключения, т.к yfinance больше не поддерживает работу с pandas, почему я не знаю
# tickers = ['AAPL', 'MSFT', 'GOOG']  # названия компаний на бирже
# tickers_name = ['Apple', 'Microsoft', 'Google']  # соответственно их названия

ticker_name=str(input('Введите название компании '))
ticker=str(input('Введите название компании, в формате на торгах(например AAPL) '))

# запрос на yahoo.finance о статистике за 2021 год для компании с названием ticker_symbol
def get_statistics(ticker_symbol):
    raw_data = yf.download(ticker_symbol, start=start_date, end=end_date)
    raw_data.index = pd.to_datetime(raw_data.index)
    values = {raw_data.index[row]: int(raw_data.values[row][0]) for row in range(raw_data.values.shape[0])}
    return values


open_array = []

open_array = get_statistics(ticker)
plt.figure(figsize=(22, 12))  # Ш, В графика
plt.plot([*open_array.keys()], [*open_array.values()], label=ticker)
# plt.plot(range(len(open_array)), open_array, label=tickers_name[i])  # Рисуем график

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%B'))  # записываем значения по Х в формате ДД-ММ
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # отслеживаем месяц
plt.xticks(rotation='vertical')  # записываем даты вертикально


plt.title(f'График цены открытия для {ticker_name}')
plt.show()


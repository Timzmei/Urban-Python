import requests
import pandas as pd

def main():
    # Библиотека requests. Получение куков с сайта httpbin.org
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    cookies = {'session_token': '123456789'}
    response = requests.get('https://httpbin.org/cookies',cookies=cookies, headers=user_agent)
    
    print('Status Code: ', response.status_code)
    # print('Text: ', response.text)
    print('encoding: ', response.encoding)
    
    data = {
        'Name': ['Anton', 'Sergei', 'Masha'],
        'Age': [30, 25, 35],
        'City': ['Moscow', 'Ekaterinburg', 'Tumen']
    }

    df = pd.DataFrame(data)

    csv_file_path = 'module11\Обзор сторонних библиотек Python\data.csv'

    df.to_csv(csv_file_path, index=False)



    data = pd.read_csv(csv_file_path)

    print("Первые 3 строки данных:")
    print(data.head())

    print("Информация о данных:")
    print(data.info())

    print("Статистика данных:")
    print(data.describe())

    print("Количество строк и столбцов в данных:")
    print(data.shape)
    
    
    
if __name__ == "__main__":
    main()
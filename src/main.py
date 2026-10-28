# Импорт load_dotenv.
from dotenv import load_dotenv 

# Импорт библиотеки для работы с окружением.
import os  

# Загрузка переменных из .env
load_dotenv(dotenv_path='.env')

print('Hello from main!')

def print_author():
    # Допишите здесь ваш код
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}") 


print_author()


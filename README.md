# TestMail.ru

Задача: Практическая самостоятельная работа по тестированию главной страница mail.ru.

Основные функции, которые необходимо протестировать:
1. Поиск информации.
2. Проверка доступности новостей.
3. Авторизация почты.

Отчет: 

1. Поиск осуществляется.

2. Новости открываются, а именно:
  - главная новость;
  - обычная новость;
  - переход в новости региона;
  - главная новость региона;
  - обычная новость региона.
А так же.
После открытия каждой новости, новость открывалась новой вкладкой. Научился использовать переход между вкладками и после открытия новости, закрытие вкладки.

3. Авторизацию проходит и делает проверку, есть ли кнопка "выход".

26.12.2019 Добавил новый тест test_guest_read_all, в котором используется новая функция guest_read_all_first_news.
В данной функции реализован цикл, который проходит по всем главным новостям в разделе "Новости".

Первоначальные задачи: 
1. Усовершенствовать функцию, которая открывает все новости. Для этого потребовалось: 
       - найти универсальный селектор, который будет работать и на топ новость и на второстепенные, а так же функционировать с циклом for
       Селектор: f".news.news_x-xs div:nth-child({i + 1}) a"

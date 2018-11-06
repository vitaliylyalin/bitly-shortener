# Обрезка ссылок с помощью Битли
Быстро сокращает ссылки, используя сервис Bitly:
```
[in] python bitly-shortener.py https://dvmn.org/modules/web-api/lesson/migration-from-website/
[out] bit.ly/2FASbRT
```
Или возвращает общее количество кликов по вашей короткой ссылке:
```
[in] python bitly-shortener.py bit.ly/2FASbRT
[out] Total clicks for this link: 12
```
Все полученные пары **длинная ссылка : короткая ссылка** кешируются в локальную базу данных:
```
{"_default": {"1": {
"long_link": "https://dvmn.org/modules/web-api/lesson/migration-from-website/",
"short_link": "bit.ly/2FASbRT"}}}
```
В дальнейшем, при попытке сократить ссылку, которую мы сократили ранее, скрипт вернёт короткую ссылку из локальной базы.
### Как установить
Для начала нужно получить личный токен **Bitly**, для этого необходимо [зарегистрироваться](https://bitly.com/a/sign_up?utm_content=site-free-button&utm_source=organic&utm_medium=website&utm_campaign=null&utm_cta=site-free-button).
Далее в настройках аккаунта найти **Generic Access Token** и сгенерировать токен.
Токен необходимо сохранить в файл с именем .env в корне проекта:
```
BITLY_TOKEN=<ваш токен>
```
Туда же, ниже строкой, необходимо внести имя базы данных:
```
CACHE_DB=<придумайте имя>
```
Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
[in] pip install -r requirements.txt
```
### Использование
Вызов справки:
```
[in] python bitly-shortener.py -h
```
Сокращение ссылки:
```
[in] python bitly-shortener.py https://dvmn.org
```
Ссылка обязательно должна содержать имя протокола ```http://``` или ```https://```, иначе выдаст предупреждение:
```
[out] This is not a valid link.
```

А вот короткие ссылки можно указывать так:
```
[in] python bitly-shortener.py https://bit.ly/2FASbRT
```
Или так:
```
[in] python bitly-shortener.py bit.ly/2FASbRT
```
Количество кликов отображается за всё время существования короткой ссылки:
```
[out] Total clicks for this link: 35
```
Или не отображается, если кликов нет:
```
[out] There is no clicks for this link
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

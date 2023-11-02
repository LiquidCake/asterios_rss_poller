# RSS helper for Lineage 2 Asterios 

This script starts HTTP server with a single endpoint that proxies requests to RSS feed of Asterios Lineage 2 server - in order to help RSS readers to get more stable responses and provide updates ASAP.  
It performs re-tries and allows to filter for event you actually need (e.g. kills of Cabrio)

- Launch script on any system your phone can access by IP address (like remote server or just a PC that is connected to the same network as your phone, if router allows access etc.)  
- Setup RSS client on your phone (like this one https://play.google.com/store/apps/details?id=com.madsvyat.simplerssreader&hl=en&gl=US - not affiliated)  
- Set URL of your server as a source of RSS feed, configure sync. time to some small value (but DONT set less than like 30-20s to avoid blocking by Asterios)  
e.g. if your PC's ip in a home netwok is `192.168.100.15` then set RSS URL as `http://192.168.100.15:8080/cabrio,heka` (/cabrio,heka - path can contain name of any event from event from RSS feed)  
If you open the same URL (e.g. `http://192.168.100.15:8080/cabrio,heka`) in your phone's browser - you could check that your RSS proxy server is working and is available through network. Result should be the same as on Asterios (e.g. `https://asterios.tm/index.php?cmd=rss&serv=0&out=xml`, but with your events filter)  
- Make sure your PC (server) is turned ON for the whole time you are waiting for event (boss) - as it will proxy each request from the phone to Asterios server   

### How to launch script (server):  
Find URL of RSS feed for L2 server you are playing on:  
1. open this in browser: https://asterios.tm/index.php?cmd=rss&serv=0  
2. select your server on that web page (x5, x7 etc), copy URL from browser address bar and add trailing `&out=xml`

Use resulting URL as an argument for this script (use quotes)  
Launched from command line console like this:  
`python asterios_rss_poller.py "https://asterios.tm/index.php?cmd=rss&serv=0&out=xml"`  

if Python script is used directly - install required dependencies (`pip install -r requirements.txt`)  
if Windows standalone exe is used - then just run `asterios_rss_poller.exe "https://asterios.tm/index.php?cmd=rss&serv=0&out=xml"`  
(exe packed script is considered malware by antiviruses)  

TCP port by default is 8080, to change it - pass port as 2nd command line argument  

------------------------------

Данный скрипт запускает HTTP сервер с единственным эндпоинтом (адресом), который проксирует запросы к RSS ленте Астериос Lineage 2 сервера - для того чтобы предоставить клиентским приложениям для чтения RSS более стабильный доступ к ленте, и помочь получать обновления как можно раньше  
Он производит повторыные попытки соединиться с сервером и позволяет фильтровать ленту и получать только нужные события (напр. убийства Cabrio)  

- Запустите скрипт на любой системе, к которой ваш телефон может присоединиться по сети (по IP) - например удалённый сервер или просто ПК, который подключен к той же сети, что и телефон (если роутер не блокирует такие соединения)  
- Установите RSS клиент на телефон (например такой - https://play.google.com/store/apps/details?id=com.madsvyat.simplerssreader&hl=en&gl=US)  
- Укажите URL вашего сервера в качестве источника RSS ленты, сконфигурируйте время синхронизации на некоторое небольшое значение (но НЕ ставьте меньше 30-20сек, чтобы избежать блокировки Астериосом)  
напр. если IP вашего ПК в домашней сети `192.168.100.15` то укажите RSS URL как  `http://192.168.100.15:8080/cabrio,heka` (/cabrio,heka - путь может содержать имя любого интересующего события из RSS ленты)  
Открыв тот же самый URL (напр. `http://192.168.100.15:8080/cabrio,heka`) в браузере на телефоне - вы сможете убедиться что ваш RSS прокси сервер работает и доступен по сети. Результат должен быть такой же как на Астериосе (напр. `https://asterios.tm/index.php?cmd=rss&serv=0&out=xml`, но с вашим фильтром событий)  
- Убедитесь что ваш ПК (сервер) остаётся включенным всё время, пока вы ожидаете событие (босса) - т.к. он будет проксировать каждый запрос от телефона к Астериосу

### Как запустить скрипт (сервер):
Получите URL RSS ленты для L2 сервера, на котором вы играете:   
1. в браузере откройте https://asterios.tm/index.php?cmd=rss&serv=0  
2. выберите свой сервер на открывшейся странице (x5, x7 итп), скопируйте URL из адресной строки и добавьте в конец `&out=xml`

Используйте полученный URL в качестве аргумента командной строки для данного скрипта (заключите URL в кавычки)  
Запустите скрипт из командной строки (консоли), вот так:  
`python asterios_rss_poller.py "https://asterios.tm/index.php?cmd=rss&serv=0&out=xml"`  

если вы запускаете скрипт прямо через Python - установите необходимые зависимости (`pip install -r requirements.txt`)  
если вы используете самостоятельный exe для Windows - просто выполните `asterios_rss_poller.exe "https://asterios.tm/index.php?cmd=rss&serv=0&out=xml"`  
(упакованный в exe скрипт определяется антивирусами как malware)  

TCP порт по умолчанию - 8080, если нужен другой - укажите в качестве 2го аргумента командной строки

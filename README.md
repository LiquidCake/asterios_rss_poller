# RSS proxy server for Lineage 2 Asterios / RSS прокси сервер для Lineage 2 Asterios

This Python script starts local HTTP server with a single endpoint that proxies requests to RSS feed of Asterios Lineage 2 server - in order to help RSS readers to get more stable responses and provide updates ASAP.  
It performs re-tries and allows to filter for event you actually need (e.g. kills of Cabrio)

- Launch proxy server script (see below - "How to launch script (server)") on any system your phone can access by IP address (like remote server or just a PC that is connected to the same network as your phone, if router allows access etc.)  
- Setup RSS client on your phone (like this one https://play.google.com/store/apps/details?id=com.madsvyat.simplerssreader&hl=en&gl=US - not affiliated)  
configure sync. time to some small value (but DONT set less than like 30-20s to avoid blocking by Asterios)  
- Set URL of proxy server as a source of RSS feed inside your RSS client - e.g. if your PC's ip in a home netwok is `192.168.100.15` then set RSS URL as `http://192.168.100.15:8080/cabrio,heka`
(/cabrio,heka - path can contain name of any event from event from RSS feed or just `http://192.168.100.15:8080/,` for unfiltered feed)  
If you open the same URL (e.g. `http://192.168.100.15:8080/cabrio,heka`) in your phone's browser - you could check that your RSS proxy server is working and is available through network. Result should be the same as on Asterios (e.g. `https://asterios.tm/index.php?cmd=rss&serv=0&out=xml`, but with your events filter)
If you cant find IP address of your PC - check console output after proxy server is launched  
- Make sure your PC (server) is turned ON for the whole time you are waiting for event (boss) - as it will proxy each request from the phone to Asterios server   

### How to launch script (server):  
- Download proxy server script:
  exe for windows - https://github.com/LiquidCake/asterios_rss_proxy/releases/download/1.0/asterios_rss_poller.exe  
  python script for any platform - https://github.com/LiquidCake/asterios_rss_proxy/archive/refs/tags/1.0.zip  
- Find URL of RSS feed for L2 server you are playing on:  
  1. open this page in browser: https://asterios.tm/index.php?cmd=rss&serv=0  
  2. select your server on that web page (x5, x7 etc), copy URL from browser address bar and add trailing `&out=xml`
  3. use resulting URL as an argument for this script (use quotes)  

Launch from command line console like this:  
`asterios_rss_poller.exe "https://asterios.tm/index.php?cmd=rss&serv=0&out=xml"`  
(python script packed as windows standalone .exe - is considered malware by some antiviruses)  
  
or like this:  
`python asterios_rss_poller.py "https://asterios.tm/index.php?cmd=rss&serv=0&out=xml"`  
if Python script is used directly - install required dependencies (`pip install -r requirements.txt`)  

TCP port by default is 8080, to change it - pass port as 2nd command line argument  

------------------------------

![ip](https://github.com/LiquidCake/asterios_rss_proxy/assets/9273621/21572bb7-fc55-4eb7-b8d5-b7b1eb358561)

------------------------------

Данный скрипт запускает локальный HTTP сервер с единственным эндпоинтом (адресом), который проксирует запросы к RSS ленте Астериос Lineage 2 сервера - для того чтобы предоставить клиентским приложениям для чтения RSS более стабильный доступ к ленте, и помочь получать обновления как можно раньше  
Он производит повторные попытки соединиться с сервером и позволяет фильтровать ленту и получать только нужные события (напр. убийства Cabrio)  

- Запустите скрипт прокси сервера (см. ниже - "Как запустить скрипт (сервер)") на любой системе, к которой ваш телефон может присоединиться по сети (по IP) - например удалённый сервер или просто ПК, который подключен к той же сети, что и телефон (если роутер не блокирует такие соединения)  
- Установите RSS клиент на телефон (например такой - https://play.google.com/store/apps/details?id=com.madsvyat.simplerssreader&hl=en&gl=US)  
сконфигурируйте время синхронизации на некоторое небольшое значение (но НЕ ставьте меньше 30-20сек, чтобы избежать блокировки Астериосом)   
- Укажите URL прокси сервера в качестве источника RSS ленты в вашем RSS клиента - напр. если IP вашего ПК в домашней сети `192.168.100.15` то укажите RSS URL как `http://192.168.100.15:8080/cabrio,heka`  (/cabrio,heka - путь может содержать имя любого интересующего события из RSS ленты, или `http://192.168.100.15:8080/,` для ленты без фильтров)  
Открыв тот же самый URL (напр. `http://192.168.100.15:8080/cabrio,heka`) в браузере на телефоне - вы сможете убедиться что ваш RSS прокси сервер работает и доступен по сети. Результат должен быть такой же как на Астериосе (напр. `https://asterios.tm/index.php?cmd=rss&serv=0&out=xml`, но с вашим фильтром событий)
Если вы не можете найти IP адрес своего ПК - посмотрите в вывод консоли после запуска прокси сервера
- Убедитесь что ваш ПК (сервер) остаётся включенным всё время, пока вы ожидаете событие (босса) - т.к. он будет проксировать каждый запрос от телефона к Астериосу

### Как запустить скрипт (сервер):
- Скачайте скрипт прокси сервера:
  exe для windows - https://github.com/LiquidCake/asterios_rss_proxy/releases/download/1.0/asterios_rss_poller.exe  
  python скрипт для любой платформы - https://github.com/LiquidCake/asterios_rss_proxy/archive/refs/tags/1.0.zip  
- Получите URL RSS ленты для L2 сервера, на котором вы играете:   
  1. в браузере откройте https://asterios.tm/index.php?cmd=rss&serv=0  
  2. выберите свой сервер на открывшейся странице (x5, x7 итп), скопируйте URL из адресной строки и добавьте в конец `&out=xml`  
  3. используйте полученный URL в качестве аргумента командной строки для данного скрипта (заключите URL в кавычки)  

Запустите скрипт из командной строки (консоли), вот так:  
`asterios_rss_poller.exe "https://asterios.tm/index.php?cmd=rss&serv=0&out=xml"`  
(python скрипт, упакованный как самостоятельный windows .exe - определяется как malware некоторыми антивирусами)  

или так:  
`python asterios_rss_poller.py "https://asterios.tm/index.php?cmd=rss&serv=0&out=xml"`  
если вы запускаете python скрипт напрямую - установите зависимости (`pip install -r requirements.txt`) 

TCP порт по умолчанию - 8080, если нужен другой - укажите в качестве 2го аргумента командной строки

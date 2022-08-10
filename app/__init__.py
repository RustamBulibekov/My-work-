from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login3'

from app import routes, models


"""Сценарий выше просто создает объект приложения как экземпляр класса Flask, импортированного из пакета flask. 
Переменная __name__, переданная в класс Flask, является предопределенной переменной Python,
 которая задается именем модуля, в котором она используется. Flask использует расположение модуля, 
 переданного здесь как отправную точку, когда ему необходимо загрузить связанные ресурсы,
  такие как файлы шаблонов, которые я расскажу в главе 2. Для всех практических целей передача __name__ почти всегда 
  будет настраивать flask в правильном направлении. Затем приложение импортирует модуль routes, 
  который еще не существует.
  "Один из аспектов, который может показаться запутанным вначале, состоит в том, что существуют два объекта с именем app. Пакет приложения определяется каталогом приложения и сценарием __init__.py и указан в инструкции routes импорта приложения. Переменная app определяется как экземпляр класса Flask в сценарии __init__.py, что делает его частью пакета приложения.


Другая особенность заключается в том, что модуль routes импортируется внизу, а не наверху скрипта, 
как это всегда делается. Нижний импорт является обходным путем для циклического импорта, что является общей проблемой 
при использовании приложений Flask. Вы увидите, что модуль routes должен импортировать переменную приложения, 
определенную в этом скрипте, поэтому, поместив один из взаимных импортов внизу, вы избежите ошибки, которая возникает 
из взаимных ссылок между этими двумя файлами.

Так что же входит в модуль routes? routes — это разные URL-адреса, которые приложение реализует. 
В Flask обработчики маршрутов приложений записываются как функции Python, называемые функциями просмотра. 
Функции просмотра сопоставляются с одним или несколькими URL-адресами маршрутов, поэтому Flask знает, какую логику 
следует выполнять, когда клиент запрашивает данный URL-адрес."""

@ECHO OFF
start /B C:\"Program Files (x86)"\Google\Chrome\Application\chrome.exe "http://127.0.0.1:8000/" 
cmd /k "cd Scripts & activate & cd .. & cd src & python manage.py runserver"


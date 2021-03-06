"""

git init - .git (данная папка является скрытой и в ней содержатся все необх.файлы наешго репозитория
git remote add name url (HTTPS или SSH ссылку) она добавляет удаленный репозитарий который находится на каком либо сервере
git pull origin master (стягивает изменения с какой либо ветки (в данном случае с ветки master)
git status (показывает статус файлов проектов)
git add (добавляет файлы в рабочей папке staging area  для дальнейшего коммита)
git add name file (добавит только файл name file)
git add .(добавит все файлы в staging area)
git commit (добавляет все файлы которые находятся в staging area(index) во внутреннюю БД и сохраняет их слепок то есть их состоние на текущий момент и сдвигает указатель текущей ветки на этот слепок
обычно набирают git commit -m "comment"
git branch (менеджер веток - можно посмотреть список веток и выбрать необходимую ветку)
git branch name branch (создать новую ветку c названием name branch)
git checkout name branch (прозводит на ветку с имененм name branch)
git push name branch (отправка кода в удаленный репозиторий)
git push origin master (в первое время будем часто это использовать когда будем работать со своим репозиторием)
git reset filename (удаление файла filename из индекса то есть из staging area)
git log - просмотр историй изменений комитов


"""

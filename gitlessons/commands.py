from ast import main
from mimetypes import init


GIT - распределенная система контроля версий 
Это система для отлеживания ведения истории изменений виших фалов или проекта.

Репозиторий - хранилище ваших файлов который вы отслеживаете при помощи гита, и их изменение.

Команда Git:

GIT- распределение системы контроля версий

1. git init - она создает новый гит репозиторий локально на вашем пк, создаст она в той директории где вы запускаете эту команду (запускается только один раз)

2. Git add - когда мы создаем изменяем файлы то при помощи этой команды мы загружаем все измещения в промежуточные место хранение 
git add <file name>
git add . - все в текущей директорий 

git commit - как только мы достигаем до определенного момента в разработке, то мы тогда сохраняем и комментируем все наши изменения в репозиторий. 
(Фиксация изменение в репо)

git commit -m '<comments>'

git remote add - это команда для того чтобы связать ваш локальный репозиторий с удаленными репозиторием в гитхабе

git remote add <названия подключение> <ссылка на репозиторий> 

git remote add origin <url>

5. git push  - после коммита изменений при помощи этой команды мы отправляем наши изменения в файлах на удаленный репозиторий

git push <origin> <название ветки(main)>

git push origin main
--------------------------------------------------------------------------
1. git init
2. git banch -M (переимыновываем главную ветку с master на main)
3. git add .
4. git commit -m 'comment' (все добавлено в лок репр)
5. git remoti add origin <url>
6. git push origin main
/////////////////////////////
git add .
git commit -m 'comment'
git push origin main 
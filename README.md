

**Steps to Run Project**

**Download Project and Extact it.**

**Step 1**
>>Open VSCode and Open the Folder.
>>Open mysql table creation queries.docx (location : Gabriels>mysql table creation queries.docx)
>>Copy Queries and Paste it in the Workbench
>>Then it Execute.
>>Now Create Database and Table then will Insert data.

**Note**
>>We have used longblob field for userprofile image
  1.Use Local Directory Required Images Must stored in (C:\ProgramData\MySQL\MySQL Server 8.0\Uploads) path to Display Image.
  Because, that is MySQL Server Environmental Path.
  (If any doubts will appear, you can See that document (mysql table creation queries.docx)).

**Step 2**
>>In VSCode
>>Open _Settings.py_

**Add this things in this settings.py**

*from  pathlib import path,os
*import pymysql ## import pymysql for models creation for already exist table
*pymysql.install_as_MySQLdb() ## database installation

*In Database - 'default': {'ENGINE': 'django.db.backends.mysql',
                              'NAME': ' <your DB_name>',
                              'USER':'<your username> ',
                              'PASSWORD':'<your password> ',
                              'HOST':'<'your localhost'> ',
                              'PORT':'<your portnumber>'}
                              
*In TEMPLATE=[
              .....
              in 'DIRS':[os.path.join(BASE_DIR,'template')
              .....

]

*INSTALLED_APPS = [
    ....
    
    'app'### include application name to execute
]

>>Open cmd Prompt
>>**pip install pymysql for create model as Exist Table 
>>**pip install pybase64

**Step 3**
>>Open VSCode Terminal or cmd Prompt in project location 
>>**py manage.py runserver
  

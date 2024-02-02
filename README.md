Running the Aplication :

1. Open a terminal console in the working "url_shortener" directory and paste there : "docker-compose build"
2. After the build finished paste : "docker-compose up"
3. Meanwhile, open another terminal in the working directory "url_shortener" and paste : "docker exec -it url_shortener /bin/bash"

4. In the opened terminal paste : "python manage.py migrate" ->
(If an error occurred like "django.db.utils.ProgrammingError: relation {table_name} already exists" then leave
this process as the database should have migrated with the files i sent in the docker volumes, in case i forgot to delete them)

5. Now you can access "127.0.0.1:8000" in the web. An admin user is already created in the migration files, so you just need to use the credentials
 - username : admin
 - password : admin
 -> Now you can use the API Documentation

6. All the links can be accessed through PostMan, but i suggest accessing the "/url_shortener_api/<shortened_code>" through the web as it provides rendering

Running Tests : 

1. Open a terminal console in the working directory "url_shortener" and paste : "docker exec -it url_shortener /bin/bash"
2. Execute there this command : "python manage.py test -v2 --keepdb url_shortener_api.tests"

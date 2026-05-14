CHECKING IF THIS WORKS
 correct email or not
## django setup 
![djangosetup](images/Screenshot%202026-05-09%20at%2014.56.39.png)

# created super user and adding the screenshot of /admin
![superuser admin](images/Screenshot%202026-05-11%20at%2013.14.58.png)


# Listing database tables 
                  List of relations
 Schema |            Name            | Type  | Owner 
--------+----------------------------+-------+-------
 public | auth_group                 | table | user
 public | auth_group_permissions     | table | user
 public | auth_permission            | table | user
 public | auth_user                  | table | user
 public | auth_user_groups           | table | user
 public | auth_user_user_permissions | table | user
 public | django_admin_log           | table | user
 public | django_content_type        | table | user
 public | django_migrations          | table | user
 public | django_session             | table | user
(10 rows)

# listing the contents of static files 
divyashrestha@alunos292 QuizHub %  source /Users/divyashrestha/Document
s/Project/QuizHub/QuizHub/.venv/bin/activate
(.venv) divyashrestha@alunos292 QuizHub % ls
README.md               env.db.example
docker                  images
docker-compose.yml      oms
(.venv) divyashrestha@alunos292 QuizHub % cd oms
(.venv) divyashrestha@alunos292 oms % ls
db.sqlite3      manage.py       oms             staticfiles
(.venv) divyashrestha@alunos292 oms % cd staticfiles
(.venv) divyashrestha@alunos292 staticfiles % ls
admin
(.venv) divyashrestha@alunos292 staticfiles % cd admin
(.venv) divyashrestha@alunos292 admin % ls
css     img     js
(.venv) divyashrestha@alunos292 admin % cd css
(.venv) divyashrestha@alunos292 css % ls
autocomplete.css                nav_sidebar.css
base.css                        responsive.css
changelists.css                 responsive_rtl.css
dark_mode.css                   rtl.css
dashboard.css                   unusable_password_field.css
forms.css                       vendor
login.css                       widgets.css
(.venv) divyashrestha@alunos292 css % cd ..
(.venv) divyashrestha@alunos292 admin % ls
css     img     js
(.venv) divyashrestha@alunos292 admin % cd img
(.venv) divyashrestha@alunos292 img % ls
LICENSE                 icon-no.svg
README.txt              icon-unknown-alt.svg
calendar-icons.svg      icon-unknown.svg
gis                     icon-viewlink.svg
icon-addlink.svg        icon-yes.svg
icon-alert.svg          inline-delete.svg
icon-calendar.svg       search.svg
icon-changelink.svg     selector-icons.svg
icon-clock.svg          sorting-icons.svg
icon-deletelink.svg     tooltag-add.svg
icon-hidelink.svg       tooltag-arrowright.svg
(.venv) divyashrestha@alunos292 img % cd..
zsh: command not found: cd..
(.venv) divyashrestha@alunos292 img % cd ..
(.venv) divyashrestha@alunos292 admin % ls
css     img     js
(.venv) divyashrestha@alunos292 admin % js
zsh: command not found: js
(.venv) divyashrestha@alunos292 admin % cd js
(.venv) divyashrestha@alunos292 js % ls
SelectBox.js                    inlines.js
SelectFilter2.js                jquery.init.js
actions.js                      nav_sidebar.js
admin                           popup_response.js
autocomplete.js                 prepopulate.js
calendar.js                     prepopulate_init.js
cancel.js                       theme.js
change_form.js                  unusable_password_field.js
core.js                         urlify.js
filters.js                      vendor
(.venv) divyashrestha@alunos292 js % 

## adding page params
![page params](images/Screenshot%202026-05-13%20at%2014.58.47.png)


### checking if the static page works fine
![static page] (images/Screenshot 2026-05-14 at 18.23.05.png)
# To do app

## Python - Django 

- Model-View-Template architecture.
- Full authentication : Register-Login-Logout.
- Create-Read-Update-Delete.
- Django templating language-HTML-CSS

### Deployed with Heroku --> [https://www.youtube.com/watch?v=XZoTukqekzY&ab_channel=CodeWithTomi](https://www.youtube.com/watch?v=XZoTukqekzY&ab_channel=CodeWithTomi)

## Deployed Link --> [https://todolistbydiala.herokuapp.com/](https://todolistbydiala.herokuapp.com/)


## Notes:

- Must create a folder by the name of the app directly inside templates, put your html components there,, the templates folder must be in root directory, asign it inn settings.py/BASE_DIR = ['templates'].

-  this class is placed inside the model to keep the incomplete tasks at the top of the list.

```
    class Meta:
        ordering = ['complete']
```

- This import inside views is used to redirect the user to specific route,, in some views can be replaced with (success_url) attribute: `success_url = "/"` , other views must be places within a function: ```def get_success_url(self):
        return reverse_lazy('tasks')```

```
from django.urls import reverse_lazy
```


- This is very important to lead only authenticated users to login, else won't work.

```
redirect_authenticated_user = True
```

- when deploying, should migrate by heroku after flushing the database,, run:

```
python manage.py flush

heroku run python manage.py migrate
```


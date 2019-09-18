# Django


__STEP 1__

---

1. C:\Users\Grv>pip install django

2. E:\>mkdir HOla

3. E:\>cd Hola


4. E:\HOla>django-admin startproject First


5. E:\HOla>cd First

E:\HOla\First>dir
 Volume in drive E has no label.
 Volume Serial Number is D63B-A887

 Directory of E:\HOla\First

09/18/2019  10:17 PM    <DIR>          .
09/18/2019  10:17 PM    <DIR>          ..
09/18/2019  10:17 PM    <DIR>          First
09/18/2019  10:17 PM               646 manage.py
               1 File(s)            646 bytes
               3 Dir(s)  315,422,736,384 bytes free

6. E:\HOla\First>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 18, 2019 - 22:18:19
Django version 2.2.5, using settings 'First.settings'
Starting development server at http://127.0.0.1:8000/


---



__STEP 2__

---

1. python manage.py startapp Mobile

2.  Added the name of the app in settings.py

3. Add a line in settings.py

```python
        'DIRS': [os.path.join(BASE_DIR, '/templates')],

```

4. Mapping urls
  
  * Create urls.py for my app Mobile

```python 
from django.urls import path
from . import views


urlpatterns=[
  path('',views.home,name='homepage')
]
```

  * In Projects urls.py include the apps urls.py

```python

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Mobile.urls')),
]


```

5. Added my view named home in views.py . View is just a function

```python

from django.shortcuts import render

# Create your views here.


def home(request):
  return render(request,'home.html',{})


```

6. Added the home.html within templates directory

```html

<!DOCTYPE html>
<html>
<head>
  <title></title>
</head>
<body>
  <h1>Hello world</h1>
</body>
</html>
```

---
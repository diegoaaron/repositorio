# base.html 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" integrity="sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l" crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'css/index.css' %}" />
    <title>Web Title</title>
</head>
<body>
    <div class="container-fluid">
        <div>
            <h1 class="text-white text-center">{% block title %}{% endblock %}</h1>
            <div class="card p-5">
                {% block content %}
                {% endblock %}
            </div>
        </div>
    </div>
</body>
</html>
```
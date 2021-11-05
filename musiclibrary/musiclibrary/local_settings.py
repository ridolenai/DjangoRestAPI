SECRET_KEY = 'django-insecure-_=&i7&dt)a68wgmc3%v*ele(c=+icksi6%-6e)av!)ir4-5zsn'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'Password3141',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True            
        }
    }
}
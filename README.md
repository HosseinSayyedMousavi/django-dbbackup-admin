# django-dbbackup-admin
get backup from database through admin panel

This is a simple and useful method to get backup from database through admin panel

### 1. install package
    pip install django-dbbackup-admin

### 2. add this packages in INSTALLED_APPS :
```
INSTALLED_APPS = [
    # ...
    'dbbackup',
    'solo',
    'dbbackup_admin'
    # ...
]
```
### 3.read documents of django-dbbackup library from this link :
    https://django-dbbackup.readthedocs.io/en/master/

### 4. set your desired config like this:
```
DBBACKUP_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DBBACKUP_STORAGE_OPTIONS = {
    'access_key': config("S3_ACCESS_KEY"),
    'secret_key':config("S3_SECRET_KEY"),
    'bucket_name': config("S3_BUCKET_NAME"),
    'default_acl': config("S3_DEFAULT_ACL"),
    'location':config("S3_BACKUP_FOLDER_NAME")
}
```
Note: If you use s3 storage you should install boto3 package.
### 5. create and migrate migrations in BASE_DIR: 
    python manage.py makemigrations dbbackup_admin
    python manage.py migrate dbbackup_admin

when you pass this missions toy will see this in your admin panel:
![Panel](https://github.com/HosseinSayyedMousavi/django-dbbackup-admin/assets/104124540/fca21688-e377-45f4-846d-7b2adede191b)


when you click on save button backup will be saved on your desired bucket or directory.

Thanks for attention

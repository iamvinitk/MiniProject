"""
==>> View sql create statements
=> python manage.py sqlmigrate <app_name> <migration_id>
output:
E:\Django\MiniProject>python manage.py makemigrations kompany
Migrations for 'kompany':
  kompany\migrations\0001_initial.py
    - Create model User

E:\Django\MiniProject>python manage.py sqlmigrate kompany 0001
BEGIN;
--
-- Create model User
--
CREATE TABLE "kompany_user" (
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        "name" varchar(250) NOT NULL,
        "password" varchar(100) NOT NULL,
        "email" varchar(250) NOT NULL);
COMMIT;

<!---------------------------------------------------------------------!>

==>> Create site Admin user
==> python manage.py createsuperuser

from django.template.defaultfilters import slugify
for obj in MyModel.objects.all():
...     obj.slug = slugify(obj.title)
...     obj.save()
"""
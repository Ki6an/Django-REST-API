from django.db import models

# we are creating class, that has the fields which are the column of the db table.

class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title


'''
to see the sql code execute this command: 
                 python manage.py sqlmigrate books 0001 
                                          <app name> <migration file name>
                                                     | usually starts with 0001
 '''

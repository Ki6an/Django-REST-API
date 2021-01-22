from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User


# class UserProfileManager(BaseUserManager):
#     """ helps django work with our custom user model """

#     def create_user(self, email, name, password=None):
#         """ Creates new user profile object """

#         if not email:
#             raise ValueError('Users must have an email address.')

#         email = self.normalize_email(email)

#         user = self.model(email=email, name=name)

#         user.set_password(password)
#         user.save(using=self._db)

#         return user


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

# class UserProfile(AbstractBaseUser, PermissionsMixin):
#     """ Represents a user profile inside our system. """

#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BinaryField(default=False)

    # # objects = UserProfileManager()

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['name']

    # def get_full_name(self):
    #     """ Used to get a users full name. """
    #     return self.name

    # def get_short_name(self):
    #     """ Used to get a users short name """
    #     return self.name

    # def __str__(self):
    #     """ django uses this to convert a object to string """
    #     return self.email

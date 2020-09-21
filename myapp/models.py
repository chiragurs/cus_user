from django.db import models
from django.contrib.auth.models import \
    BaseUserManager,AbstractBaseUser
# Create your models here.

class UserModel(AbstractBaseUser):
    email=models.EmailField(
        max_length=100,
        unique=True,
        verbose_name="email address",
    )

    active=models.BooleanField(default=True)
    staff=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)
    USERNAME_FIELD='email'
    REQURIED_FIELD=[]

    def get_full_name(self):
        #the user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email
    
    def __str__(self):      #__unicode__ on python 2
        return self.email
    
    def has_perm(self,perm,obj=None):
    "Does the user have a specific permisssion?"
        #simplest possible answer:yes,always
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        "is user a member of staff"
        return self.staff
    
    @property
    def is_admin(self):
        "is user a admin member"
        return self.admin
    
    @property
    def is_active(self):
        "Is user active"
        return self.active


    



          
#UserManager Class
class UserManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user=self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self,email,password):
        """Creates and saves a staff user with given email and password."""
        user=self.create_user(
            email,
            password=password,
        )
        user.staff=True
        user.save(using=self._db)
        return user

    
    def create_superuser(self,email,password):
        """Creates and saves a superuser with the given email and password"""
        user=self.create_user(
            email,
            password=password,
        )
        user.staff=True
        user.admin=True
        user.save(using=self._db)
        return user
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):

    # patient
    def create_user(self, email, password, firstname=None, lastname=None):
        if not email:
            raise ValueError('User must have an email')
        
        if not password:
            raise ValueError('User must have a password')

        user = self.model(
            email = self.normalize_email(email)
        )

        user.set_password(password)
        user.firstname = firstname
        user.lastname = lastname
        user.save(using=self._db)

        return user

    # admin
    def create_superuser(self, email, password):
        
        user = self.create_user(
            email,
            password=password,
            
        )
        user.admin = True
        user.save(using=self._db)

        return user

    # patient
    def create_patient(self, email, password, firstname, lastname):
        
        user = self.create_user(
            email,
            password=password,
            
        )
        user.firstname = firstname
        user.lastname = lastname
        user.patient = True
        user.save(using=self._db)

        return user

    # hospital
    def create_hospital(self, email, password, firstname):
        
        user = self.create_user(
            email,
            password=password,
        )
        user.hospital = True
        user.firstname  = firstname
        user.save(using=self._db)

        return user
    
    # doctor
    def create_doctor(self, email, password, firstname, lastname):
        
        user = self.create_user(
            email,
            password=password
        )
        user.doctor = True
        user.firstname = firstname
        user.lastname = lastname
        user.save(using=self._db)

        return user


    



class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=300)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    admin = models.BooleanField(default=False)
    hospital = models.BooleanField(default=False)
    doctor = models.BooleanField(default=False)
    patient = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        if self.firstname != None:
            return self.firstname
        else:
            return self.email 

    def has_perm(self, perm, obj=None):
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_admin(self):
        return self.admin
    
    # @property
    # def is_hospital(self):
    #     return self.hospital
    
    # @property
    # def is_doctor(self):
    #     return self.doctor

    # @property
    # def is_patient(self):
    #     return self.patient
    
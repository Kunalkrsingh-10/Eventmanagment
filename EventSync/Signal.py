from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,post_init,pre_delete,post_delete,pre_save,post_save
from django.core.signals import request_started,request_finished,got_request_exception

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("---------------------------------")
    print("Login successful signal.......")
    print("Request:", request)
    print("Sender:", sender)
    print("User:", user)
    print("User password : ", user.password)
    print(f'Kwargs: {kwargs}')

#user_logged_in.connect(login_success, sender=User) it's sescond method to connect above method is using decorator to connect signal is also right 

@receiver(user_logged_out, sender=User)
def log_out(sender, request, user, **kwargs):
    print("---------------------------------")
    print("Logout successful signal.......")
    print("Request:", request)
    print("Sender:", sender)
    print("User:", user)
    print(f'Kwargs: {kwargs}') 

@receiver(user_login_failed)
def login_faild(sender, request, credentials, **kwargs):
    print("---------------------------------")
    print("Login faild signal .......")
    print("Request:", request)
    print("Sender:", sender)
    print("Credential:", credentials)
    print(f'Kwargs: {kwargs}')   
    user_login_failed.connect(login_faild) #manual method to connect signal 

@receiver(pre_save, sender=User)
def before_save(sender, instance, **kwargs):
    print("---------------------------------")
    print("before save it will call  .......")
    print("Sender:", sender)
    print("Instance:", instance)
    print(f'Kwargs: {kwargs}') 

@receiver(post_save, sender=User)
def After_save(sender, created, instance, **kwargs):
    if created :
     print("---------------------------------")
     print("After save it will call  .......")
     print("New record add in database")
     print("Sender:", sender)
     print("Instance:", instance)
     print(f'Kwargs: {kwargs}')
    else : 
     print("---------------------------------")
     print("After save it will call  .......")
     print("No new record add in db")
     print("Sender:", sender)
     print("Instance:", instance)
     print(f'Kwargs: {kwargs}')          


@receiver(pre_init, sender=User)
def before_save(sender, *args, **kwargs):
    print("---------------------------------")
    print("Pre init signal , befor start djanog app  .......")
    print("Sender:", sender)
    print(f'Args:{args}')
    print(f'Kwargs: {kwargs}') 

@receiver(post_init, sender=User)
def before_save(sender, *args, **kwargs):
    print("---------------------------------")
    print("Post init signal , after started djanog app  .......")
    print("Sender:", sender)
    print(f'Args:{args}')
    print(f'Kwargs: {kwargs}') 

@receiver(request_started)
def At_begining_request(sender,environ,**kwargs):
   print("---------------------------------")
   print("Signal before requesting   .......")
   print("Sender:", sender)
   print("Enviro",environ)
   print(f'Kwargs: {kwargs}')  

@receiver(request_finished)
def After_request(sender,**kwargs):
   print("---------------------------------")
   print("Signal before requesting   .......")
   print("Sender:", sender)
   print(f'Kwargs: {kwargs}')    

@receiver(got_request_exception)
def At_beginin(sender,request ,**kwargs):
   print("---------------------------------")
   print("Signal before requesting   .......")
   print("Sender:", sender)
   print("Request:", request)
   print(f'Kwargs: {kwargs}')    
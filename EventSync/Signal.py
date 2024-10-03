from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import employees_info
import threading

@receiver(post_save, sender=employees_info)
def after_save_employee(sender, instance, created, **kwargs):
    current_thread = threading.current_thread().name
    print(f"Signal running in thread: {current_thread}")

    if created:
        print(f"Employee {instance.name} created!")
        # Simulate raising an exception within the transaction to cause rollback
        raise Exception("Simulated error to rollback transaction")
    else:
        print(f"Employee {instance.name} updated!")

@receiver(post_delete, sender=employees_info)
def after_delete_employee(sender, instance, **kwargs):
    print(f"Employee {instance.name} deleted!")

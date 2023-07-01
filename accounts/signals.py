"""
The Django Signals is a strategy to allow decoupled applications to get
notified when certain events occur. Let’s say you want to invalidate a 
cached page everytime a given model instance is updated, but there are 
several places in your code base that this model can be updated. You can 
do that using signals, hooking some pieces of code to be executed everytime this specific model’s save method is trigged.
"""


from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Customer
from django.dispatch import receiver
from django.contrib.auth.models import Group

#instance = user
@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):

	if created:
		group = Group.objects.get(name='customer')
		instance.groups.add(group)

		Customer.objects.create(
			user = instance,
			name = instance.username,
			)

		#Customer.objects.create(user=instance)
		print('Profile created!')

#post_save.connect(create_customer, sender=User)

"""
@receiver(post_save, sender=User)
def update_customer(sender, instance, created, **kwargs):

	if created == False:
		#instance.customer.save()
		print('profile updated!')

#post_save.connect(update_customer, sender=User)
"""
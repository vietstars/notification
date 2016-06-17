from celery import Task

#from django.conf import settings
from django.db.models import Max
from django.db.models import Min

from apps.notifications import models

import random

class CreateNotifications(Task):
	"""
	Creates institute objects based on the given json data.
	"""

	def run(self, *args, **kwargs):

		upper_limit = models.MyUser.objects.all().aggregate(Max('id'))
		lower_limit = models.MyUser.objects.all().aggregate(Min('id'))

		## select a user to be notified randomly

		to_user = None
		to = 0
		
		while to_user is None:

			to = random.randint(lower_limit['id__min'], upper_limit['id__max'])

			try:
				to_user = models.MyUser.objects.get(id=to)
			except:
				pass



		## select a user to be notified from randomly

		frm_user = None
		frm = to

		while frm_user is None:
			
			while frm == to:
				frm = random.randint(lower_limit['id__min'], upper_limit['id__max'])
			
			try:
				frm_user = models.MyUser.objects.get(id=frm)
			except:
				pass

		notif_type = ['comment on', 'liked', 'shared']
		notif_media = ['post', 'picture', 'video']

		models.Notification.objects.create(
			user = to_user,
			notifier = frm_user,
			notification_type = random.choice(notif_type),
			notification_media = random.choice(notif_media))

		to_user.new_notification_count += 1
		to_user.save()
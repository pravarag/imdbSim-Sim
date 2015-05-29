from django.db import models

from django.contrib.auth.models import User




class UserProfile(models.Model):

	user = models.OneToOneField(User)		##oneToOne means only one user

	def __unicode__(self):
		return self.user.username


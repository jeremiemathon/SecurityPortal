from django.db import models
from django import forms
from django.db import models
from django.utils  import timezone
from django.contrib.auth.models import User
from django.contrib import admin
from django.urls import reverse

from ckeditor.fields import RichTextField

from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey
# Create your models here.


class Section(SortableMixin):
    title = models.CharField(max_length=255, default='Section Title')
    description = models.TextField(default='')
    # order = models.IntegerField(default=0)
    section_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    # rules = models.ForeignKey(to=Rule)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['section_order',]

class Needs(models.Model):
	title = models.CharField(max_length=255, default='Security Needs')
	description = models.TextField(default='')
	level = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name="Security Needs - (Confidentiality, Integrity, Availability)"
		verbose_name_plural="Security Needs - (Confidentiality, Integrity, Availability)"

class Rule(SortableMixin):
	title = models.CharField(max_length=255, default='')
	# section = models.CharField(max_length=255, default='')
	section = SortableForeignKey(to=Section, on_delete=models.CASCADE, null=True)
	# content = models.TextField()
	content = RichTextField()
	date_posted = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	mandatory = models.BooleanField(default=True)
	rule_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
	# needs = models.ForeignKey(Needs, on_delete=models.CASCADE)


	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('rule-detail', kwargs={'pk':self.pk})
	class Meta:
		ordering = ['rule_order',]
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


class Policy(SortableMixin):
	title = models.CharField(max_length=255, default='Section Title')
	description = RichTextField()
	order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['order', ]

	def get_absolute_url(self):
		return reverse('policy-list')

	pass


class Section(SortableMixin):
	title = models.CharField(max_length=255, default='Section Title')
	description = RichTextField()
	order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
	policy = SortableForeignKey(to=Policy, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['order', ]


class SubSection(SortableMixin):
	title = models.CharField(max_length=255, default='Section Title')
	description = RichTextField()
	order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
	section = SortableForeignKey(to=Section, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['order', ]


class Needs(models.Model):
	title = models.CharField(max_length=255, default='Security Needs')
	description = models.TextField(default='')
	level = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Security Needs - (Confidentiality, Integrity, Availability)"
		verbose_name_plural = "Security Needs - (Confidentiality, Integrity, Availability)"


class Rule(SortableMixin):
	title = models.CharField(max_length=255, default='')
	subsection = models.ForeignKey(to=SubSection, on_delete=models.CASCADE,  blank=True, null=True)
	section = models.ForeignKey(to=Section, on_delete=models.CASCADE, blank=True, null=True)
	content = RichTextField()
	date_posted = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	mandatory = models.BooleanField(default=True)
	order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('rule-detail', kwargs={'pk': self.pk})

	class Meta:
		ordering = ['order', ]


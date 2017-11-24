#!/usr/bin/env python3
#coding:utf-8

from django import forms
from comments.models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'url', 'text']
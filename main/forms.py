# -*- coding:utf-8 -*-
# author:aoaoc
# datetime:7/7/2019 12:10 PM
# software: PyCharm

from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(label="name", max_length=200)
    check = forms.BooleanField(initial=False, required=False)



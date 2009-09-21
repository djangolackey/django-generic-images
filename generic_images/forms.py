#coding: utf-8

from django.forms import ModelForm
from generic_images.models import AttachedImage


class AttachedImageForm(ModelForm):    
    ''' Simple form for AttachedImage model with ``image`` and ``caption`` fields.'''
    
    class Meta:
        model = AttachedImage
        fields = ['image', 'caption']
        

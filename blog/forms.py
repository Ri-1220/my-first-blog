from django import forms

from .models import Post, Meeting

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('train',)

class MeetingForm(forms.ModelForm):
    class Meta():
        model = Meeting
        fields = ('train1', 'time1',)
# 'train2', 'time2', 'train3', 'time3', 'train4', 'time4', 'train5', 'time5',
        

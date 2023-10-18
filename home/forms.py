from django import forms
from .models import Profile, BlogPost,Rating,Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_no', 'bio', 'facebook', 'instagram', 'linkedin', 'image', )
     
        
from django import forms
from .models import BlogPost, Category

class BlogPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Select a category', widget=forms.Select(attrs={'class': 'form-control'}))


    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'content', 'image', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
        }

        

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('rating',)
        widgets = {
            'rating': forms.NumberInput(attrs={'min': '0', 'max': '6'}),
        }

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating > 6:
            raise forms.ValidationError("Rating must be 6 or less.")
        return rating
    
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        
        
class EditBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image']
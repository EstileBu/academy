from django.forms import ModelForm
from .models import Review
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment', 'movie']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-reviewForm'
        self.helper.form_class = 'reviewFormCSSClass'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_review'

        self.helper.add_input(Submit('submit', 'Submit'))
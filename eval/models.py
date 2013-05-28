from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

def validate_eval_score(value):
    if (value < 0) or (value > 3):
        raise ValidationError(u'%s must be between 0 and 3' % value)

CASE_CATEGORIES = (
    ('breast', 'Breast'),
    ('repro_female', 'Female Repro'), 
    ('repro_male', 'Male Repro'),
    ('gi', 'GI'),
    ('lung', 'Lung'),
    ('neuro', 'Neuro'),
    ('renal', 'Renal'),
)

# Create your models here.
class CaseEvaluation(models.Model):
    resident = models.ForeignKey(User)
    difficulty = models.IntegerField(validators=[validate_eval_score])
    diagnostic_accuracy = models.IntegerField(validators=[validate_eval_score])
    completeness = models.IntegerField(validators=[validate_eval_score])
    case_category = models.CharField(max_length=50, choices=CASE_CATEGORIES, null=True, blank=True)
    evaluation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s %s" % (self.evaluation_date, self.resident.username)

from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

def validate_eval_score(value):
    if (value < 0) or (value > 3):
        raise ValidationError(u'%s must be between 0 and 3' % value)

# Create your models here.
class CaseCategory(models.Model):
    title = models.CharField(max_length=100)
	
    def __unicode__(self):
        return self.title


class CaseEvaluation(models.Model):
    resident = models.ForeignKey(User)
    difficulty = models.IntegerField(validators=[validate_eval_score])
    diagnostic_accuracy = models.IntegerField(validators=[validate_eval_score])
    completeness = models.IntegerField(validators=[validate_eval_score])
    case_category = models.ForeignKey(CaseCategory, null=True, blank=True)
    evaluation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s %s" % (self.evaluation_date, self.resident.username)

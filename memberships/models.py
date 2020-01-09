from django.db import models
from django.conf import settings

MEMBERSHIP_CHOICES = (
    ('ENTERPRISE','ent'),
    ('PROFESSIONAL','pro'),
    ('FREE','free')
)
class Membership(models.Model):
    slug = models.SlugField()
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES,default="free",max_length=20)
    price = models.IntegerField(default=15)
    stripe_plan_id = models.CharField(max_length=50)

    def __str__(self):
        return self.membership_type


class UserMembership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50)
    membership = models.OneToOneField(Membership,on_delete=models.CASCADE)

class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership,on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
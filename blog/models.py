from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# class userDetails(models.Model):
#     youName = models.CharField(max_length=50)
#     loverName = models.CharField(max_length=50)
#     youActivity = models.CharField(max_length=50)
#     loverActivity = models.CharField(max_length=50)
#     favColor = models.IntegerField(default=0)
#     favDrink = models.IntegerField(default=0)
#     favTouch = models.IntegerField(default=0)
#     loverGender = models.IntegerField(default=0)

#     def __str__(self):
#         return ' '.join([
#             self.youName,
#             self.loverName,
#             self.youActivity,
#             self.loverActivity,
#             self.favColor,
#             self.favDrink,
#             self.favTouch,
#             self.loverGender
#             ])




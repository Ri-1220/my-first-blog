from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    
#    title = models.CharField(max_length=200)
#    text = models.TextField()
#   created_date = models.DateTimeField(
#           default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    train = models.CharField(max_length=100)

 #   def publish(self): #ブログを公開するメソッド
 #       self.published_date = timezone.now()
 #       self.save()

#def __str__(self): #ポストのタイトルのテキストを返す
#        return self.title


class Meeting(models.Model):
    LINE_CHOICES = (
        ('marunouti','東京メトロ丸ノ内線'),
        ('hukutosi','東京メトロ副都心線'),
        ('sinjuku','都営新宿線'),
        ('ooedo','都営大江戸線'),
        ('yamanote','JR山手線'),
        ('soumu','JR総武線'),
        ('saikyou','JR埼京線'),
        ('tyuou','JR中央線'),
        ('tyuouhon','JR中央本線'),
        ('syounansinjuku','湘南新宿ライン'),
        ('keiou','京王線'),
        ('keiousin','京王新線'),
        ('odakyuuodawara','小田急小田原線'),
        ('seibusinjuku','西武新宿線'),
    )
    
    #目的地の有無
    destination = models.IntegerField()
    #ランドマークか出口の名前
    landmark = models.CharField(max_length=30)
    #1人目の路線
    train1 = models.CharField(max_length=15,choices=LINE_CHOICES,default='marunouti',)
    #1人目の到着時間
    time1 = models.TimeField(default=timezone.now)
    """
    #2人目の路線
    train2 = models.CharField(max_length=15,choices=LINE_CHOICES,default='marunouti',)
    #2人目の到着時間
    time2 = models.TimeField(default=timezone.now)
    #3人目の路線
    train3 = models.CharField(max_length=15,choices=LINE_CHOICES,default='marunouti',)
    #3人目の到着時間
    time3 = models.TimeField(default=timezone.now)
    #4人目の路線
    train4 = models.CharField(max_length=15,choices=LINE_CHOICES,default='marunouti',)
    #4人目の到着時間
    time4 = models.TimeField(default=timezone.now)
    #5人目の路線
    train5 = models.CharField(max_length=15,choices=LINE_CHOICES,default='marunouti',)
    #5人目の到着時間
    time5 = models.TimeField(default=timezone.now)
"""

def __str__(self): #ポストのタイトルのテキストを返す
        return self.train1
    
    

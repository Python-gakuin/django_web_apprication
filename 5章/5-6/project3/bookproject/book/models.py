from django.db import models

CATEGORY = (('business', 'ビジネス'), ('life', '生活'), ('other', 'その他'))
class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(
        max_length=100,
        choices=CATEGORY
    )

    # class Meta:
    #     verbose_name = '本のデータ'
    # 上は、一度コードを書くがすぐに消すためコメントアウトしています。

    def __str__(self):
        return self.title
    
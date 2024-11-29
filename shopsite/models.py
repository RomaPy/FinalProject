from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=70, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    # осталось определить к какому виду относится продукт: овощи, фрукты или мясо.
    # Для этого создаём кортеж с типами:
    TYPE = [
        ('VEG', 'Овощи'),
        ('FRU', 'Фрукты'),
        ('MEA', 'Мясо'),
    ]
    # Теперь даём возможность выбора типа пищи из кортежа TYPE:
    type = models.CharField(choices=TYPE, max_length=3, default='VEG', verbose_name='Тип')

    # Чтобы в админке прописывались явно наши продукты сделаем преобразование
    def __str__(self):
        return self.title
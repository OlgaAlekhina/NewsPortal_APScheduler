from django.db.models.signals import m2m_changed, post_save, post_delete
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .models import Post, Category
from .tasks import news_mail
import logging

logger = logging.getLogger('news.views')

@receiver(m2m_changed, sender=Post.categories.through)
def notify_subscribers(instance, action, pk_set, *args, **kwargs):
    if action == 'post_add':
        html_content = render_to_string(
            'post_created_letter.html',
            {'post': instance}
        )
        for pk in pk_set:
            category = Category.objects.get(pk=pk)
            recipients = [user.email for user in category.subscribers.all()]
            subject=f'На сайте NewsPortal появилась новая статья: {instance.post_title}'
            from_email='olga-olechka-5@yandex.ru'
            news_mail.delay(subject, from_email, recipients, html_content)


@receiver(post_save, sender=Post)
def logging_save(sender, instance, created, **kwargs):
    if created:
        logger.info(f'A new post "{instance.post_title}" was created by {instance.post_author}.')
    else:
        logger.info(f'Post "{instance.post_title}" was changed.')


@receiver(post_delete, sender=Post)
def logging_delete(sender, instance, **kwargs):
    logger.info(f'Post "{instance.post_title}" was deleted.')

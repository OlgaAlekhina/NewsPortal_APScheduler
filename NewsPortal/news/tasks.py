from celery import shared_task
from datetime import datetime, timedelta
from .models import Category, Post
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


@shared_task
def weekly_mail():
    from_date = datetime.now() - timedelta(days=7)
    for cat in Category.objects.all():
        posts = Post.objects.filter(categories=cat).filter(post_time__gte=from_date)
        if posts.exists():
            recipients = [user.email for user in cat.subscribers.all()]
            msg = EmailMultiAlternatives(
                subject=f'Статьи за прошедшую неделю в категории "{cat.name}"',
                from_email='olga-olechka-5@yandex.ru',
                to=recipients
            )

            html_content = render_to_string(
                'weekly_mail.html',
                {'posts': posts})

            msg.attach_alternative(html_content, "text/html")
            msg.send()


@shared_task
def news_mail(subject, from_email, recipients, html_content):
    msg = EmailMultiAlternatives(
        subject=subject,
        from_email=from_email,
        to=recipients
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()
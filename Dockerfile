FROM danpalmer/danpalmer.base

ADD . /app
RUN pip install /app

RUN mkdir /app/staticfiles
RUN /app/manage.py collectstatic --noinput --clear

EXPOSE 80
CMD ["gunicorn", "danpalmer.wsgi:application"]

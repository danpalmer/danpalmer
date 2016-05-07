FROM danpalmer/danpalmer.base

ADD . /app
WORKDIR /app
RUN pip install .

RUN mkdir /app/staticfiles
RUN /app/manage.py collectstatic --noinput --clear

EXPOSE 80
CMD ["gunicorn", "-b", "0.0.0.0:80", "danpalmer.wsgi:application"]

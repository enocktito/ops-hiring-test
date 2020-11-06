FROM sedjro/quatro-api:alpha
WORKDIR /home/
COPY . .
RUN pip install -r requirements.txt
RUN mkdir -p /var/www/kele/media \
  && chmod -R 777 /var/www/kele/

FROM python:alpine

RUN apk add --no-cache --virtual .build-deps build-base \
 && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -U pip \
 && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt \
 && apk del .build-deps

CMD [ "uwsgi", "postcard.ini" ]

EXPOSE 5000

FROM python:2.7-alpine
MAINTAINER chris elliott <ctelliott@gmail.com>

# install dependencies
ADD ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# add auth
ADD ./src/* /opt/
RUN chmod +x /opt/*.py

CMD ["/opt/auth.py"]

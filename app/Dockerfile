FROM python:2

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN git clone https://github.com/pacparser/pacparser.git \
	&& cd pacparser \
	&& make -C src pymod \
	&& make -C src install-pymod

COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

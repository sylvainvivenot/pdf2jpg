FROM alpine:3.7
COPY src/requirements.txt .
RUN apk add --no-cache poppler-utils \
                       python python3 \
                       build-base \
                       python-dev python3-dev \
                       # wget dependency
                       openssl \
                       # dev dependencies
                       git \
                       bash \
                       sudo \
                       py2-pip \
                       # Pillow dependencies
                       jpeg-dev \
                       zlib-dev \
                       freetype-dev \
                       lcms2-dev \
                       openjpeg-dev \
                       tiff-dev \
                       tk-dev \
                       tcl-dev \
                       harfbuzz-dev \
                       fribidi-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY src/pdf2jpg.py .
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "pdf2jpg.py" ]


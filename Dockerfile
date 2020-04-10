FROM python:3.7-alpine

COPY MAC_Add.py /tmp/MAC_Add/
RUN pip install requests
ARG MAC_API_KEY
ENV MAC_API_KEY ${MAC_API_KEY}

ENV PATH $PATH:/tmp/MAC_Add/

WORKDIR /tmp/MAC_Add/
CMD ["/tmp/MAC_Add/MAC_Add.py"]
ENTRYPOINT ["python"]
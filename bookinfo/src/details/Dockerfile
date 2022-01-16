FROM ruby:2.7.1-slim
#RUN git clone https://github.com/vfg27/creativa2Bloque2
COPY details.rb /opt/microservices/
WORKDIR /opt/microservices
ARG service_version
ARG enable_external_book_service
ENV SERVICE_VERSION ${service_version:-v1}
ENV ENABLE_EXTERNAL_BOOK_SERVICE ${enable_external_book_service:-true}
EXPOSE 9080
CMD ["ruby","details.rb","9080"]

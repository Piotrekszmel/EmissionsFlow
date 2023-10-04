FROM postgres:latest

COPY ./schemas/*.sql /docker-entrypoint-initdb.d/

EXPOSE 5432

CMD ["postgres"]

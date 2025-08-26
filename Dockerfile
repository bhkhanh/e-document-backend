# |----------------------------|
# |--------- BUILDER ----------|
# |----------------------------|
FROM python:3.13-alpine AS builder

# set these ENVs to optimize the Python image
ENV PYTHONUNBUFFERED=1

# install dependencies
RUN pip install -U pip --no-cache-dir
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt



# |-------------------------------|
# |---------- DEV/LOCAL ----------|
# |-------------------------------|
FROM python:3.13-alpine AS dev

# copy the installed dependencies from the stage "builder" to current stage
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# set these ENVs to optimize the Python image
ENV PYTHONUNBUFFERED=1
ENV HISTFILE=/dev/null
ENV HOME=/nonexistent

# create a non-root user & assign permission to its working directory
RUN adduser -D dev_user && chown -R dev_user:dev_user /usr/src

# switch to non-root user
USER dev_user

# set working directory again
WORKDIR /usr/src

# copy files from host to the container (except files in .dockerignore)
COPY . .

# setup entry point to be the main executable
ENTRYPOINT [ "python", "manage.py" ]

# setup CMD to specify additional arguments
CMD [ "runserver", "0.0.0.0:8888" ]

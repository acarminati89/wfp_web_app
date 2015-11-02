#############################################################################
##
## Dockerfile to build an analytics instance on EC2
## Built using nano
##
#############################################################################

# Set the base image
#FROM dockerfile/python
FROM ubuntu

# Set Author
MAINTAINER Anthony Carminati, anthony@carminati.io

# Set Debian front end to noninteractive mode
ENV DEBIAN_FRONTEND noninteractive

# Refresh apt-get meta-data and install python tools
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip build-essential gunicorn
RUN apt-get install -y libxslt-dev libxml2-dev libpam-dev libedit-dev
RUN apt-get install -y awscli

# Set new working directory to application root
WORKDIR /

# Bundle app source
ADD . /src/

# Update PIP and all packages
RUN pip install -U pip
RUN pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs pip install -U

# Add and install Python modules from requirements file
RUN pip install -r /src/requirements.txt

# Expose ports
EXPOSE 22 8000

# Add Locale
RUN locale-gen en_US en_US.UTF-8
RUN dpkg-reconfigure locales

# Run application
# CMD ["python", "/src/app.py"]


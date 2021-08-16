# init a base image (Alpine is small Linux distro)
FROM python:3.8

# define the present working directory
WORKDIR /Craft-Exercise

# copy the contents into the working dir
ADD . /Craft-Exercise

# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt

# add current working directory to python path
ENV PYTHONPATH "${PYTHONPATH}:<current working directory path>"

# define the command to start the container
CMD ["python","api_template/app.py"]
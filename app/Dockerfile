# Use an official Python runtime as an image
FROM python:3.6

# The EXPOSE instruction indicates the ports on which a container
EXPOSE 5000

# Sets the working directory for following COPY and CMD instructions
WORKDIR /app

COPY requirements.txt /app
COPY templates /app/templates
COPY font-awesome.min.css /app/static/stylesheets/font-awesome.min.css

RUN python -m pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt

# Run app.py when the container launches
COPY app.py /app
CMD ["python", "-u", "app.py"]

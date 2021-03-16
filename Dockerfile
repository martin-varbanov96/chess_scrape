FROM puckel/docker-airflow:1.10.9

#   WARNING: The scripts pip, pip3 and pip3.7 are installed in '/usr/local/airflow/.local/bin' which is not on PATH.
#   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
# Successfully installed pip-21.0.1
# WARNING: You are using pip version 20.0.2; however, version 21.0.1 is available.
# You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
# 


COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# add source code
#RUN mkdir source_code
COPY . .

# add linking to source code 
#ENV PYTHONPATH "${PYTHONPATH}:source_code"
ENV PYTHONPATH=${PYTHONPATH}:/usr/local/airflow

#CMD export PATH=$PATH:$ADDITIONAL_PATH;


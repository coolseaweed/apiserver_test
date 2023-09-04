# build base image
FROM python:3.10.11-slim-buster as base
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
RUN apt-get update && apt-get install -y \
    libpq-dev gcc g++ curl wget 


# final build using pre-build subimage
FROM base AS runtime
ENV work_dir="/workspace"
WORKDIR ${work_dir}
COPY server ${work_dir}/server
COPY requirements.txt ${work_dir}/requirements.txt
COPY api_run.py ${work_dir}/run.py

RUN pip install -r requirements.txt

CMD ["python", "run.py"]
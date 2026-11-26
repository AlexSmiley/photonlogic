FROM continuumio/miniconda3:latest
RUN conda install -y -c conda-forge --override-channels pymeep numpy scipy && conda clean -afy
WORKDIR /work
ENV OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONUNBUFFERED=1
CMD ["python", "native.py", "--resolution", "30", "--out", "results/ref"]

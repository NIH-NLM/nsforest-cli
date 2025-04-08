# Dockerfile
FROM continuumio/miniconda3
WORKDIR /app
COPY . .
RUN conda env create -f environment.yml && \
    echo "source activate nsforest" > ~/.bashrc
ENV PATH /opt/conda/envs/nsforest/bin:$PATH
ENTRYPOINT ["nsforest"]

# src/nsforest/__init__.py
"""nsforest package."""


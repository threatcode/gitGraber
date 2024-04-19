FROM python:latest

# Install required dependencies
RUN apt-get update && apt-get install -y git

# Clone the gitGraber repository
RUN git clone https://github.com/threatcode/gitGraber

# Set the working directory
WORKDIR /gitGraber

# Copy setup.py to the working directory
COPY setup.py .

# Install the package using setup.py
RUN python setup.py install

# Set the entrypoint and default command
ENTRYPOINT ["python", "gitGraber.py"]
CMD ["--help"]

# Dockerfile

FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application files
COPY calculator.py .
COPY test_calculator.py .

# Install necessary packages
RUN pip install unittest

# Command to run tests
CMD ["python", "-m", "unittest", "test_calculator.py"]

FROM pytorch/pytorch:1.9.0-cuda11.1-cudnn8-runtime

WORKDIR /app

# Install dependencies
RUN pip install flask gunicorn transformers

# Copy the model and serving script
COPY model/ model/
COPY app.py .

# Expose the port the app runs on
EXPOSE 5000

# Start the application
CMD ["gunicorn", "-b", ":5000", "app:app"]

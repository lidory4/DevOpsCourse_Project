FROM python:3.14-alpine
WORKDIR /games
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/ .
RUN echo 0 > /Scores.txt
ENV SCORES_FILE=/Scores.txt
EXPOSE 5000
CMD ["python", "MainScores.py"]
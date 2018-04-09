FROM     python:3.5-alpine
ENV      DISCORD_API_KEY=<discord api key>
COPY     . /app
WORKDIR  /app
RUN      pip install -r requirements.txt
CMD      [ "python", "./moosebot.py" ]

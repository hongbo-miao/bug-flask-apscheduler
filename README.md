# Flask-APScheduler Resume Job Bug

## Setup

```sh
pip install -r requirements.txt
flask run
```

## Introduction

I have an interval job which prints number every 1 second. In the beginning the job is paused by default.

When you try to call `GET http:/localhost:5000/` or `POST http:/localhost:5000/`, it should resume the interval job.

However, in the code `scheduler.resume()` works, but `scheduler.resume_job(my_task_id)` does not work.

Here is the part of issue code: https://github.com/Hongbo-Miao/bug-flask-apscheduler/blob/main/app.py#L27-L31

## Issue Ticket

Opened the issue ticket at https://github.com/viniciuschiele/flask-apscheduler/issues/214

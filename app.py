from flask import Flask
from flask_apscheduler import APScheduler

my_num = 0


def create_app() -> Flask:
    app = Flask(__name__)
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start(paused=True)

    @scheduler.task(
        "interval",
        id="my_task_id",
        seconds=1,
    )
    def increase_my_num():
        global my_num
        print(f"my_num: {my_num}")
        my_num += 1

    @app.route("/")
    def my_num():
        global my_num

        # 1) This works
        # scheduler.resume()

        # 2) This doesn't work
        scheduler.resume_job("my_task_id")

        return {"my_num": my_num}

    return app

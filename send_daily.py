from apscheduler.schedulers.blocking import BlockingScheduler
from send_data_msg import send_coronavirus_data

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_coronavirus_data, 'interval', hours=12)

sched.start()

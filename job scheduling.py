def job_scheduling(jobs):
    # jobs: (job_id, start_time, end_time)
    jobs.sort(key=lambda x: x[2])
    result = []
    last_end = 0
    for job in jobs:
        if job[1] >= last_end:
            result.append(job)
            last_end = job[2]
    return result

jobs = [('J1', 1, 3), ('J2', 2, 5), ('J3', 4, 6), ('J4', 6, 7), ('J5', 5, 9)]
scheduled = job_scheduling(jobs)
print("Scheduled Jobs:", scheduled)

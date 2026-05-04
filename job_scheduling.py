def job_scheduling(jobs, max_deadline):
    # Step 1: Sort jobs by profit (descending)
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Create time slots
    schedule = [None] * (max_deadline + 1)

    total_profit = 0
    jobs_done = []

    # Step 2: Assign jobs to slots
    for job_id, deadline, profit in jobs:
        for slot in range(min(max_deadline, deadline), 0, -1):
            if schedule[slot] is None:
                schedule[slot] = job_id
                total_profit += profit
                jobs_done.append(job_id)
                break

    return jobs_done, total_profit, schedule   


# --- Input ---
job_list = [
    ('Job1', 2, 100),
    ('Job2', 1, 19),
    ('Job3', 2, 27),
    ('Job4', 1, 25),
    ('Job5', 3, 15)
]

max_time = 3

# --- Run ---
scheduled_jobs, profit, schedule = job_scheduling(job_list, max_time)

# --- Output ---
print(f"Scheduled Jobs: {scheduled_jobs}")
print(f"Total Profit:   {profit}")
print(f"Time Slot Allocation: {['Slot ' + str(i) + ': ' + str(job) for i, job in enumerate(schedule) if i > 0]}")
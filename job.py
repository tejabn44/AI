class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

# Function to schedule jobs to maximize profit
def job_scheduling(jobs):
    # Step 1: Sort jobs by decreasing profit
    jobs.sort(key=lambda job: job.profit, reverse=True)

    n = len(jobs)
    max_deadline = max(job.deadline for job in jobs)

    # Time slots for jobs, initialized to None
    time_slots = [None] * max_deadline

    total_profit = 0
    job_sequence = []

    for job in jobs:
        # Find a free time slot before or on the deadline
        for slot in range(min(job.deadline, max_deadline) - 1, -1, -1):
            if time_slots[slot] is None:
                time_slots[slot] = job.job_id
                total_profit += job.profit
                job_sequence.append(job.job_id)
                break

    return job_sequence, total_profit

# Taking input from the user
n = int(input("Enter number of jobs: "))
jobs = []
for i in range(n):
    job_id = input(f"Enter Job ID for job {i+1}: ")
    deadline = int(input("Enter deadline: "))
    profit = int(input("Enter profit: "))
    jobs.append(Job(job_id, deadline, profit))

# Call the scheduling function
scheduled_jobs, max_profit = job_scheduling(jobs)

# Display results
print("\nScheduled Jobs (in order):", scheduled_jobs)
print("Maximum Profit:", max_profit)

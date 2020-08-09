def main():
    with open("jobs.txt") as file:
        num_jobs = int(file.readline())
        jobs = []
        for line in file.readlines():
            weight, length = line.split(" ")
            jobs.append((int(weight), int(length)))

    sorted_jobs = greedySchedule(jobs, "ratio")
    print(computeCompletionTime(jobs, sorted_jobs))


def greedySchedule(jobs, key = 'difference' or 'ratio'):
    jobs_schedule = []
    if key == "difference":
        for job in jobs:
            weight, length = job
            score = weight - length
            jobs_schedule.append((score, weight))
    else:
        for job in jobs:
            weight, length = job
            score = weight / length
            jobs_schedule.append((score, weight))
    
    # sorts the jobs by index
    sorted_jobs = sorted(range(len(jobs_schedule)), key = jobs_schedule.__getitem__)
    sorted_jobs.reverse()
    return sorted_jobs


def computeCompletionTime(jobs, sorted_jobs):
    finish_time = 0
    weighted_sum = 0
    for i in sorted_jobs:
        finish_time += jobs[i][1]
        weighted_sum += finish_time*jobs[i][0]
        
    return weighted_sum


if __name__=="__main__":
    main()
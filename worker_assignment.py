# using python
# Import the random libraries for use in generating random data
import random
# Dynamically generate the workers data
num_workers = random.randint(400,1000)
workers = []
# Generate the list of workers with random salaries
for i in range(numworkers):
    worker = {
        "name": f"Worker{i+1}",
        "gender": random.choice(["Male", "Female"]),
        "salary": random.randint(3000, 40000)
    }
    workers.append(worker)
# Assign the workers level based on salary and gender
def assign_worker_level(salary, gender):
    if salary > 10000 and salary < 20000:
        return "A1"
    elif salary > 7500 and salary < 30000 and gender == 'Female':
        return "A5-F"
    else:
        return "unassigned"
# for loop to generate payment slip for all workers
for worker in workers:
    try:
        salary = worker['salary']
        gender = worker['gender']
        employee_level = assign_worker_level(salary, gender)
        print(f"{worker['name']} - Gender: {gender} - Salary: ${salary} - Employee Level: {employee_level}")
    except Exception as e:
        print(f"Error processing {worker['name']}: {e}")
## Notes
- The random seed is not set in this script, so you'll get different results each time you run it.
- The salary range and level assignment criteria can be easily modified in the script to suit different requirements.

## Future Improvements
- Add command-line arguments for customizing the number of workers or salary range.
- Implement data export to CSV or other formats.
- Create visualizations of the salary distribution or level assignments.
- Add more sophisticated error handling and logging.

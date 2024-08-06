# linkedin to review job requirements and make spreadsheeet to ort by company -> automate (arash script?)
# webscraping w/ beautiful soup and job alerts and input into spreadsheet
# Webscrape positions experience application outlines
# Automated linkedin scraper
# Job application auto fill -> teal and wonsulting tools
# job tracker base:
from send_email import send_email

URL = "https://remoteok.io/api"
keys = ["date", "company", "position", "tags", "location", "url"]

wanted_tags = ["python"]  # remote, javascript, backend, mobile, ...
# regex expression here for finding matches related to job


def get_jobs():
    resp = requests.get(URL)
    job_results = resp.json()

    jobs = []
    for job_res in job_results:
        # take only the specified keys
        job = {k: v for k, v in job_res.items() if k in keys}

        if job:
            tags = job.get("tags")
            tags = {tag.lower() for tag in tags}
            if tags.intersection(wanted_tags):
                jobs.append(job)

    return jobs


if __name__ == "__main__":
    python_jobs = get_jobs()

    if python_jobs:
        message = "Subject: Remote Python Jobs!\n\n"
        message += "Found some cool Python jobs!\n\n"

        for job in python_jobs:
            message += f"{json.dumps(job)}\n\n"

        send_email(message)

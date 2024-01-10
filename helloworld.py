from prefect import flow, task, get_run_logger

@task
def hello():
    return("Hello from Prefect.")
    

@flow(name="Hello World")
def runner(source_bucket, destination_bucket):
    logger = get_run_logger()
    logger.info(hello)

if __name__ == "__main__":
    runner()

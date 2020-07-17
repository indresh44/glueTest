import unittest
import sys
import boto3
import filecmp
import time

glue = boto3.client('glue')


def runJob(jobname):
	response = glue.start_job_run(JobName=jobname)
	jobRunid = response['JobRunId']
	response = glue.get_job_run(JobName=jobname,RunId=jobRunid)
	state = response['JobRun']['JobRunState']
	print("state " + state)
	while state == 'RUNNING':
		time.sleep(180)
		response = glue.get_job_run(JobName=jobname,RunId=jobRunid)
		state = response['JobRun']['JobRunState']
		print("state " + state)
	print("final state " + state)
	return state

class MyTestCase(unittest.TestCase):
  def test_glue(self):

      # Remove the hardcoded value, take as a parameter. Right now hardcoded for demo purpose.
      job_name = "GlueCsvToParq"
      print("start execurint job test")
      self.assertEqual(runJob(job_name), 'SUCCEEDED')


if __name__ == '__main__':
  # if len(sys.argv) > 1:
  #       MyTestCase.STACKNAME = sys.argv.pop()
  unittest.main()

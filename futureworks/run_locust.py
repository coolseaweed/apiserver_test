from locust import HttpUser,task,between 

class AppUser(HttpUser):
	wait_time = between(0.1,0.5)

	# Endpoint
	@task
	def home_page(self):
		self.client.get("/v1/dummy")

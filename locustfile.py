from locust import HttpUser, task, constant

class HelloWorldUser(HttpUser):
    wait_time = constant(1)

    @task
    def hello_world(self):
        self.client.get("https://api-microservices.sfportal.com/_/healthz")
#        self.client.get("https://api-microservices.sfportal.com/_/readyz")
#        self.client.get("http://a661777e4b52f4ea2ad90bb6392cce0e-9064b8fda52262ca.elb.us-west-2.amazonaws.com/_/readyz")
#        self.client.get("http://a661777e4b52f4ea2ad90bb6392cce0e-9064b8fda52262ca.elb.us-west-2.amazonaws.com/_/healthz")


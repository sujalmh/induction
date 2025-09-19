from locust import HttpUser, task, between

class ChallengeUser(HttpUser):
    wait_time = between(1, 2)  # wait between requests

    @task
    def prompt_test(self):
        self.client.post(
            "/api/challenge/prompt",
            json={"prompt": "hey"},
            headers={"Content-Type": "application/json"}
        )

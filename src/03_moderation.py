from util import client

response = client.moderations.create(
    input="Here's the plan. We get the warhead and we hold the world ransom for... ONE MILLION DOLLARS!"
)
moderation_output = response.results[0].to_dict()

breakpoint()

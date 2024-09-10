from util import get_completion, get_completion_and_token_count

delimeter = "####"
system_message = f"""
You will be provided with customer service queries. The customer service query will be delimited with {delimeter} character.

Classify each query into a primary category and a secondary category.

Provide your output in json format with the keys: primary and secondary.

Primary categories: Billing, Technical Support, Account Management, or General Inquiry.

Billing secondary categories:
Unsubscribe or upgrade
Add a payment method
Explanation for charge
Dispute a charge

Technical Support secondary categories:
General troubleshooting
Device compatibility
Software updates

Account Management secondary categories:
Password reset
Update personal information
Close account
Account securit

General Inquiry secondary categories:
Product information
Pricing
Feedback
Speak to a human
"""

user_message_01 = "I want you to delete my profile and all of my user data"
user_message_02 = "Tell me more about your flat screen TVs"
user_message_03 = "I'm having trouble with my password. Can you help me reset it?"

user_message_04 = "My computer is overheating and the fan is too noisy. I need help with this. Also, can I trade it in for a newer model?"
user_message_05 = "I thought your staff at the store was very helpful. I would like to give them a compliment."

messages = [
    {"role": "system", "content": system_message},
    {
        "role": "user",
        "content": f"{delimeter}{user_message_01}{delimeter}{user_message_02}{delimeter}{user_message_03}{delimeter}{user_message_04}{delimeter}{user_message_05}{delimeter}",
    },
]

breakpoint()

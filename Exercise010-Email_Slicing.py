email_id=input("Enter your email id: ")

index=email_id.index("@")
username=email_id[:index]
# username=email_id[:email_id.index("@")]
domain=email_id[index+1:]
# domain=email_id[email_id.index("@"):]

print(f"Your username is {username} and your domain is {domain}")
print(f"Your username is {email_id[:index]} and your domain is {email_id[index+1:]}")












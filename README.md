# EmailNator Wrapper

This is a Python wrapper for the [EmailNator](https://www.emailnator.com) website, which creates temporary Gmail email addresses.

## Important Note

This Python wrapper is developed solely for educational and testing purposes. It's intended to demonstrate API interaction and serve as a learning tool for developers interested in working with web services. We strongly encourage users to visit and support the original [EmailNator](https://www.emailnator.com) website. The creators of EmailNator provide a valuable service, and this project is not meant to replace or compete with their offering in any way.

## Features

- Generate temporary Gmail email addresses
- Retrieve messages for generated email addresses

## Installation

```bash
pip install emailnator-wrapper
```

## Usage

```python
from emailnator_wrapper import EmailnatorWrapper

# Create an instance of the wrapper
emailnator = EmailnatorWrapper()

# Generate a temporary email address
email = emailnator.generate_email()
print(f"Generated email: {email}")

# Wait for messages to arrive (optional)
import time
time.sleep(10)

# Retrieve messages
messages = emailnator.get_messages(email)
for msg in messages:
    print(f"From: {msg.get('from', 'Unknown sender')}")
    print(f"Subject: {msg.get('subject', 'No subject')}")
    print(f"Time: {msg.get('time', 'No time')}")
    print("-" * 40)
```

## Educational Purpose

This project is designed to help developers learn about:
- Interacting with web APIs
- Handling authentication and session management
- Processing JSON responses
- Building reusable Python classes

We encourage users to explore the code, understand how it works, and use it as a starting point for their own projects or learning experiences.

## Support the Original Service

If you find this wrapper useful, please consider using and supporting the official [EmailNator](https://www.emailnator.com) service. They provide the infrastructure and service that makes this educational project possible.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This wrapper is not officially associated with EmailNator. Use it responsibly and in accordance with EmailNator's terms of service. The authors of this wrapper are not responsible for any misuse or any consequences arising from the use of this software.
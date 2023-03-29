messages = ['hi, how are you?', 'whaddup?', 'oh what a beautiful morning']
sent_messages = []


def send_messages(messages):
    while messages:
        message = messages.pop(0)
        print(f"Sending message: {message}")
        sent_messages.append(message)


send_messages(messages[:])
print(messages)
print(sent_messages)

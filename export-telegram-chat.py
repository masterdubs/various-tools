# install telethon first: pip install telethon

from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest

# Replace these with your own values that you can find here: https://my.telegram.org/apps
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
group_username = 'GROUP_USERNAME_OR_ID'


# Setting up the client
client = TelegramClient('session_name', api_id, api_hash)

async def export_chat_history():
    await client.start()
    print("Client Created")

    # Ensuring you are authorized
    if not await client.is_user_authorized():
        phone = input('Enter your phone number: ')
        await client.send_code_request(phone)
        await client.sign_in(phone, input('Enter the code: '))

    # Accessing the group
    group = await client.get_entity(group_username)
    
    # Asking for number of messages or 'all' for full export
    user_input = input("Enter the number of messages to export or type 'all' for full history: ").strip().lower()
    export_all = user_input == 'all'
    num_messages = int(user_input) if user_input.isdigit() else None

    # Fetching the history
    all_messages = []
    last_id = 0  # Initialize last_id to 0

    while True:
        if export_all or (num_messages and len(all_messages) < num_messages):
            limit = 100 if export_all else min(100, num_messages - len(all_messages))
            messages = await client.get_messages(group, limit=limit, max_id=last_id)
            if not messages:
                break
            all_messages.extend(messages)
            last_id = messages[-1].id  # Update last_id to the last message's id
        else:
            break

    # Reverse the list of messages for chronological order
    all_messages.reverse()

    # Writing messages to a file
    with open('chat_history.txt', 'w', encoding='utf-8') as file:
        for message in all_messages:
            file.write(f"{message.sender_id}: {message.text}\n")

    print('Chat history exported successfully.')

# Running the script
with client:
    client.loop.run_until_complete(export_chat_history())

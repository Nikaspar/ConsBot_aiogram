def read_token():
    with open('token') as tk:
        token = tk.read().replace('\n', '')
    return token

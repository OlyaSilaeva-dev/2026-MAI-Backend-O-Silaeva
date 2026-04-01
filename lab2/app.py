import random
import string
import time

def generate_password():
    length = random.randint(8, 16)
    
    digit = random.choice(string.digits)
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    special = random.choice("#.,!@&^%*")
    
    all_chars = string.digits + string.ascii_lowercase + string.ascii_uppercase + "#.,!@&^%*"
    remaining_length = length - 4
    remaining = ''.join(random.choice(all_chars) for _ in range(remaining_length))
    
    password_list = list(digit + lower + upper + special + remaining)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

def app(environ, start_response):
    password = generate_password()
    
    time.sleep(0.05)
    
    response_body = f"Generated password: {password}\n".encode('utf-8')
    
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain; charset=utf-8'),
        ('Content-Length', str(len(response_body)))
    ]
    
    start_response(status, response_headers)
    return [response_body]

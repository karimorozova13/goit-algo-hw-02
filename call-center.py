from queue import Queue

q = Queue()

def generate_request(id):
    request = f"Request {id}"
    q.put(request)
    print(f"Generated: {request}")

def process_request():
    if q.empty():
        print('Queue is empty.')
    else:
        print(f"Processed: {q.get()}")
      

def main():
    print('Welcome to call chat. How can we help you?')
    id =1
    options = ["1. Generate Request","2. Process Request", "3. Exit"]
    for option in options:
        print(option)
    while True:
        cmd =input("Enter your request >>>>>")
        
        if cmd in '3':
            print('Good bye')
            break
        elif cmd in '2': 
            process_request()
        elif cmd in '1':
            generate_request(id)
            id += 1
        else:
            print('Invalid option. Please enter 1, 2, or 3.')


if __name__ == '__main__':
    main()
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def generate_primes(limit):
    prime_dict={}
    count=0
    for i in range(limit+1):
        if is_prime(i):
            prime_dict[count]=i
            count+=1
    return prime_dict

def show_all(primes_dirct):
    for k,v in primes_dirct.items():
        print(f"prime number #{k} = {v}")

def get_prime_by_position(primes_dirct, pos):
    if pos in primes_dirct:
        return primes_dirct[pos]
    else:
        return None

limit = int(input("Enter the limit to generate primes: "))
primes_dict = generate_primes(limit)

app_loop=True
while app_loop:
    print("\n--- Prime Number Menu ---")
    print("1. Display all primes")
    print("2. Look up a prime by position")
    print("3. Exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        show_all(primes_dict)
    elif choice==2:
        pos=int(input("enter the position:"))
        prime_number=get_prime_by_position(primes_dict, pos)
        if prime_number:
            print(f"prime number #{pos} is {prime_number}")
        else:
            print(f"there is no prime number in position #{pos}")
    elif choice==3:
        app_loop=False
    

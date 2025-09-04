import time

def make_burger(order_no)->None :
    print(f"preparing burger #{order_no}")
    time.sleep(5) #time for making the burger
    print(f"Order #{order_no} is ready")

def main():
    for i in range(3):
        make_burger(i+1)

if __name__ == "__main__" :
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"Orders completed in {elapsed :0.2f} seconds")

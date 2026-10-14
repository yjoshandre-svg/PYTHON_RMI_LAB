import Pyro5.api

HOST = "127.0.0.1"
NS_PORT = 9000


def show(label, product):
    print(f"--- {label} ---")
    print("Name: " + product.get_name())
    print("Description: " + product.get_description())
    print("Price: " + str(product.get_price()))


def main():
    try:
        ns = Pyro5.api.locate_ns(host=HOST, port=NS_PORT)

        # Same as Client.java: look up "laptop" and print its details
        laptop = Pyro5.api.Proxy(ns.lookup("laptop"))
        show("laptop", laptop)

        # Extra: the other three objects the server registered
        for name in ("ram", "bag", "charger"):
            show(name, Pyro5.api.Proxy(ns.lookup(name)))
    except Exception as e:
        print("Exception in client side: " + repr(e))


if __name__ == "__main__":
    main()

import Pyro5.api
from product import Product

HOST = "127.0.0.1"
NS_PORT = 9000          # same port the Java registry used


def main():
    print("Server is booting....")

    # We create the objects (same data as Server.java)
    p1 = Product("Laptop", "Lenovo laptop", 800000.0)
    p2 = Product("Mobile", "MI 9 mobile", 24000.0)
    p3 = Product("Bag", "Branded bag", 800.0)
    p4 = Product("Charger", "MI Charger", 230.0)

    # Daemon = the thing that listens for remote calls (like exporting objects)
    daemon = Pyro5.api.Daemon(host=HOST)

    # Register (export) every object with the daemon -> each gets a URI
    uri1 = daemon.register(p1)
    uri2 = daemon.register(p2)
    uri3 = daemon.register(p3)
    uri4 = daemon.register(p4)

    # Find the name server (the RMI registry equivalent) and bind the names
    ns = Pyro5.api.locate_ns(host=HOST, port=NS_PORT)
    ns.register("laptop", uri1)
    ns.register("ram", uri2)       # same names as Server.java
    ns.register("bag", uri3)
    ns.register("charger", uri4)

    print("Registered objects:")
    for name, uri in (("laptop", uri1), ("ram", uri2), ("bag", uri3), ("charger", uri4)):
        print(f"  {name:8s} -> {uri}")
    print("Server is ready. Waiting for clients...")

    daemon.requestLoop()    # keep running and serve clients


if __name__ == "__main__":
    main()

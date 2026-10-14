# Java RMI -> Python Pyro5 Lab

Translation of a Java RMI project (Product / ProductImpl / Server / Client)
into Python using **Pyro5** (Python Remote Objects).

## Structure

```
PYTHON_RMI_LAB/
├── product.py   # Product.java + ProductImpl.java  (remote class)
├── server.py    # Server.java                      (creates objects, registers them)
└── client.py    # Client.java                      (looks up and calls remote objects)
```

## Java RMI -> Pyro5 mapping

| Java RMI                              | Pyro5                                   |
|---------------------------------------|-----------------------------------------|
| `interface Product extends Remote`    | class decorated with `@Pyro5.api.expose`|
| `ProductImpl implements Product`      | same class in `product.py`              |
| `UnicastRemoteObject.exportObject`    | `daemon.register(obj)`                  |
| `rmiregistry 9000`                    | `python -m Pyro5.nameserver -p 9000`    |
| `registry.bind("laptop", stub)`       | `ns.register("laptop", uri)`            |
| `registry.lookup("laptop")`           | `Pyro5.api.Proxy(ns.lookup("laptop"))`  |
| `getName()`, `getPrice()`             | `get_name()`, `get_price()`             |

## Requirements

- Python 3.8+
- Pyro5: `pip install Pyro5`

## How to run (3 terminals, in this order)

**Terminal 1 - name server** (replaces `rmiregistry 9000`)
```
python -m Pyro5.nameserver -n 127.0.0.1 -p 9000
```

**Terminal 2 - server**
```
python server.py
```
Output: `Server is booting....` ... `Server is ready. Waiting for clients...`

**Terminal 3 - client**
```
python client.py
```
Output: Name, Description and Price of the laptop, then the other products.

Start the name server first, then the server, then the client. Leave the
first two running while the client runs.

## Troubleshooting

- `NamingError: Failed to locate the nameserver` - start Terminal 1 first and
  check the port is 9000.
- `Address already in use` - an old name server is still running; close it.
- On Windows use `python` (or `py`) and run commands from the project folder.

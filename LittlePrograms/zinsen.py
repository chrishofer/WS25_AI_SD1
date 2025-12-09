
def verzinsen(betrag, jahre = 1, zinsen = 10):
    print(f"Betrag:{betrag} Jahre:{jahre} Zinsen: {zinsen}")




if __name__ == '__main__':
    # Verwendung mit default Werten
    verzinsen(1000)
    verzinsen(1000,2)
    verzinsen(1000, 2, 5)

    # Betrag und Zinsen angeben - wie mache ich das?

    verzinsen(2000, zinsen = 7)
    #verzinsen(2000, zinsen=7, 20) # Nachdem ein benannter Parameter verwendet wird kann kein unbenannter verwendet werden






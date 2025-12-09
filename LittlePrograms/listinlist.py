if __name__ == '__main__':
    zahlen = [["KW40", 30000], ["KW41", 70000, 80000], ["KW42", 80000], ["KW43", 90000]]


    # wie können wir über alle elemente iterieren?
    for idx1 in range(len(zahlen)):
        print(f'Äußere Schleife Index:{idx1}')
        # print(zahlen[idx1])
        for idx2 in range(len(zahlen[idx1])):
            print(f'Innere Schleife Index:{idx2}')
            print(zahlen[idx1][idx2])
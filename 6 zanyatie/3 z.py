def F(x):
    o = str(x)
    m = o.replace(".", "")
    count = len(o) - len(m)
    print(m, ";", count)


F("это. строка с точками.")

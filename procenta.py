class Procenta():
    def vstup():
        text = "bagriel je negr cierny gazovany napoj dingoo o smaku limonky"
        return text

    def slice(text):
        sliced = []
        slovo = ""
        for i in text + " ":
            if i != " ":
                slovo += i
            else:
                sliced.append(slovo)
                slovo = ""
        return sliced
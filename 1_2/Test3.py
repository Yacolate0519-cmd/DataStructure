def checkClose(data):
    resource = {"(" : ")", 
                "[" : "]",
                "{" : "}"}
    clean_data = list(data)
    i = 0 
    while i < len(clean_data):
        if clean_data[i] in resource.keys():
            i += 1
        elif clean_data[i] in resource.values():
            if i == 0:
                return False
            prev = clean_data[i - 1]
            if prev in resource and resource[prev] == clean_data[i]:
                clean_data.pop(i)
                clean_data.pop(i - 1)
            else:
                return False
        else:
            i += 1
    return len(clean_data) == 0

if __name__ == '__main__':
    s = "[()]"
    print(checkClose(s))
def get_lps(str):
    if str == "":
        return 0
    lps = [0] * len(str)

    prevLPS, i = 0, 1
    while i < len(str):
        if str[i] == str[prevLPS]:
            lps[i] = prevLPS + 1
            prevLPS += 1
            i += 1
        elif prevLPS == 0:
            lps[i] = 0
            i += 1
        else:
            prevLPS = lps[prevLPS - 1]
    return lps

if __name__ == "__main__":
    lps = get_lps("abaecabab")
    print(lps)

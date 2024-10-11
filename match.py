def match(pattern, source):
    sind = 0
    pind = 0
    result = []

    while pind != len(pattern) or sind != len(source):
        if pind == len(pattern):
            return None

        elif pattern[pind] == "%":
            if pind == (len(pattern) - 1):
                return result + [" ".join(source[sind:])]
            else:
                accum = ""
                pind += 1
                while pattern[pind] != source[sind]:
                    accum += " " + source[sind]
                    sind += 1

                    if sind >= len(source):
                        return None

                result.append(accum.strip())

        elif sind == len(source):
            return None

        elif pattern[pind] == "_":
            result += [source[sind].strip()]
            pind += 1
            sind += 1

        elif pattern[pind] == source[sind]:
            pind += 1
            sind += 1

        else:
            return None

    return result
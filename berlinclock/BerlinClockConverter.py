__author__ = 'SekthDroid'


class BerlinClockConverter(object):
    def get_single_minutes(self, param):
        minutes = int(param.split(":")[1][1])
        if minutes is 0:
            return "OOOO"

        if minutes > 4:
            minutes -= 5

        result = "".rjust(minutes, "Y")
        if len(result) is 4:
            return result
        result = result.ljust(4, "O")
        return result

    def get_five_minutes(self, param):
        minutes = int(param.split(":")[1])
        if minutes is 0:
            return "OOOOOOOOOOO"

        result = ""
        for i in range(5, 60, 5):
            if i <= minutes:
                result += "Y"
            else:
                result += "O"

        result = list(result)
        for i in range(2, len(result), 3):
            if result[i] is not "O":
                result[i] = "R"
        return "".join(result)

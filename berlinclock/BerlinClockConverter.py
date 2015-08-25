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

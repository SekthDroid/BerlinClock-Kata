RED = "R"
OFF = "O"
YELLOW = "Y"
__author__ = 'SekthDroid'


class BerlinClockConverter(object):
    def get_single_minutes(self, param):
        minutes = int(param.split(":")[1][1])

        minutes = minutes - 5 if minutes > 4 else minutes
        result = "".rjust(minutes, "%s" % YELLOW)
        return result.ljust(4, "%s" % OFF) if len(result) < 4 else result

    def get_five_minutes(self, param):
        minutes = int(param.split(":")[1])
        result = [YELLOW if i <= minutes else OFF for i in range(5, 60, 5)]
        for i in range(2, len(result), 3):
            if result[i] is not OFF:
                result[i] = RED
        return "".join(result)

    def get_single_hours(self, param):
        hours = int(param.split(":")[0][1])
        if hours is 0:
            return "OOOO"

        hours = hours - 5 if hours > 4 else hours
        result = "".rjust(hours, RED)
        return result.ljust(4, OFF) if len(result) < 4 else result

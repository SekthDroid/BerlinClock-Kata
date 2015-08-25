RED = "R"
OFF = "O"
YELLOW = "Y"
__author__ = 'SekthDroid'


class BerlinClockConverter(object):
    def get_single_minutes(self, param):
        minutes = int(param.split(":")[1][1])
        return self.single_row(minutes)

    def get_five_minutes(self, param):
        minutes = int(param.split(":")[1])
        result = [YELLOW if i <= minutes else OFF for i in range(5, 60, 5)]
        for i in range(2, len(result), 3):
            if result[i] is not OFF:
                result[i] = RED
        return "".join(result)

    def get_single_hours(self, param):
        hours = int(param.split(":")[0][1])
        return self.single_row(hours, RED)

    def single_row(self, digit, enabled_state=YELLOW):
        digit = digit - 5 if digit > 4 else digit
        result = "".rjust(digit, enabled_state)
        return result.ljust(4, OFF) if len(result) < 4 else result

    def get_five_hours(self, param):
        hours = int(param.split(":")[0])
        result = [RED if i <= hours else OFF for i in range(5, 25, 5)]
        return "".join(result)

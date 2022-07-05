class LookAndSaySequence:

    def get_sequence(self, numbers):
        """
        takes a number
        and returns look and say sequence of that number
        :param numbers:
        :return:
        """
        repeat_number = numbers[0]
        numbers_to_look = numbers[1:]+' '
        repeat_count = 1
        sequence = ""
        for active_number in numbers_to_look:
            if active_number != repeat_number:
                sequence += str(repeat_count) + repeat_number
                repeat_count = 1
                repeat_number = active_number
            else:
                repeat_count += 1
        return sequence



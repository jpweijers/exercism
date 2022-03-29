from audioop import reverse


class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        if (any([not n.isnumeric() for n in self.card_num])):
            return False

        if len(self.card_num) < 2:
            return False

        nums = [int(n) for n in self.card_num]
        nums.reverse()

        for i, n in enumerate(nums):
            if i % 2 != 0:
                doubled = n * 2
                if doubled > 9:
                    doubled -= 9
                nums[i] = doubled

        if sum(nums) % 10 == 0:
            return True
        return False

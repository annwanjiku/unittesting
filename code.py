# write code to convert numbers to absolute values
# non string values should be accounted for
#  test code using unittest

def converttoabs(num):
    try:
        return abs(int(num))
    except ValueError as e:
        raise ValueError from e



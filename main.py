from decorators import log_decorator_with_param

if __name__ == '__main__':
    @log_decorator_with_param('logs2.txt')
    def sum(a, b):
        return a + b

    @log_decorator_with_param('logs3.txt')
    def multy(a, b):
        return a * b

    sum(0, 0)
    sum(1, 10)
    multy(1, 10)
from functools import wraps  # не забываем правильно оборачивать!


def format_error(error):
    """Format type violation message."""
    argument, value, expected_type = error
    return (
        'Bad argument type for argument "{name}":'
        ' {type} instead of {expected}'.format(  # noqa: WPS326
            name=argument,
            type=type(value),
            expected=expected_type,
        )
    )


def throw_error(*args):
    """Raise one typing violation."""
    raise TypeError(format_error(args))


def throw_errors(errors):
    """Raise one error for all typing violations."""
    raise TypeError('\n'.join(map(format_error, errors)))


def typecheck(error_callback=throw_error):
    """
    Добавляет к функции предусловие, проверяющие типы аргументов.

    Проверка типов делается на основе аннотаций, указанных в сигнатуре
    оборачиваемой функции.

    Arguments:
        error_callback - функция, получающая информацию об ошибке типизации.
        Функция принимает имя аргумента, значение и ожидаемый тип.
        Обычно error_callback ничего не возвращает, а вместо этого возбуждает
        исключение (см. реализацию по умолчанию - throw_error).

    Returns:
        Декоратор, добавляющий проверку типов к функции.

    """
    # BEGIN (write your solution here)
    @wraps(error_callback)
    def wrapper(function):
        @wraps(function)
        def inner(**kwargs):
            annotations = function.__annotations__
            for argument, value in kwargs.items():
                argument_type = annotations.get(argument)
                if argument_type and not isinstance(value, argument_type):
                    error_callback(argument, value, argument_type)
            return function(**kwargs)
        return inner
    return wrapper


    # END


def typecheck_all(error_callback=throw_errors):
    """
    Добавляет к функции предусловие, проверяющие типы аргументов.

    Проверка типов делается на основе аннотаций, указанных в сигнатуре
    оборачиваемой функции.

    Arguments:
        error_callback - функция, получающая информацию об ошибке типизации.
        Функция принимает список кортежей, описывающих все ошибки типизации.
        Каждый кортеж содержит имя аргумента, значение и ожидаемый тип.
        Обычно error_callback ничего не возвращает, а вместо этого возбуждает
        исключение (см. реализацию по умолчанию - throw_errors).

    Returns:
        Декоратор, добавляющий проверку типов к функции.

    """
    # BEGIN (write your solution here)

    def wrapper(function):
        @wraps(function)
        def inner(**kwargs):
            errors = []
            annotations = function.__annotations__
            for argument, value in kwargs.items():
                argument_type = annotations.get(argument)
                if argument_type and not isinstance(value, argument_type):
                    errors.append((argument, value, argument_type))
            if errors:
                error_callback(errors)
            return function(**kwargs)
        return inner
    return wrapper
    # END


if __name__ == '__main__':
    @typecheck_all()
    def multiply(times: int, value: (str, tuple)):
        return value * times


    print(multiply(times=10, value=(42,)))
    print(multiply(times=10, value='1'))

    # оба аргумента — не того типа
    print(multiply(times='12', value=None))

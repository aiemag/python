#!/usr/bin/python3

def partial(func, *partial_args):

    def wrapper(*extra_args):
        args = list(partial_args)
        args.extend(extra_args)

        return func(*args)

    return wrapper


def logging(year, month, day, title, content):
    print("%s-%s-%s %s:%s" % (year, month, day, title, content))


def main():
    logging("2020", "11", "11", "weather", "sunny")

    p = partial(logging, "2020", "11", "11")
    p("news", "gold in the bank has been stolen.")
    p("news", "COVID-19 has spread in nursing hospital.")


if __name__ == "__main__":
    main()

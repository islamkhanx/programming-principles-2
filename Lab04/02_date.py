import datetime


def five_days_from_now() -> datetime.date:
    """subtract five days from current date."""

    return datetime.date.today() - datetime.timedelta(5)


def yestdy_tdy_tmrw() -> None:
    """print yesterday, today, tomorrow."""

    print(datetime.date.today() - datetime.timedelta(1))
    print(datetime.date.today())
    print(datetime.date.today() + datetime.timedelta(1))


def drop_microseconds(dt: datetime.datetime) -> datetime.datetime:
    """drop microseconds from datetime."""
    return datetime.datetime(
        dt.year, dt.month, dt.day,
        dt.hour, dt.minute, dt.second
    )


def second_difference(
    dt1: datetime.datetime,
    dt2: datetime.datetime,
) -> int:
    "calculate two date difference in seconds."
    td = dt2 - dt1
    return td.total_seconds()

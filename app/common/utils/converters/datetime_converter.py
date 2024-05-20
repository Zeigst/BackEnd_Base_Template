import pytz
from datetime import datetime, timedelta


class DatetimeConverter:
    @classmethod
    def datetime_to_epoch_ms(cls, dt: datetime):
        epoch = datetime.fromtimestamp(timestamp=0, tz=pytz.utc)
        utc_dt = dt.astimezone(pytz.utc)
        utc_dt = utc_dt.replace(tzinfo=None)
        return int((utc_dt - epoch).total_seconds() * 1000.0)

    @classmethod
    def validator_datetime_utc(cls, dt: datetime):
        if not isinstance(dt, datetime):
            return dt
        if dt.tzinfo is None:
            return dt.replace(tzinfo=pytz.utc)
        utc_dt = dt.astimezone(pytz.utc)
        return utc_dt

    @classmethod
    def format_utc_str(cls, dt: datetime):
        dt = cls.validator_datetime_utc(dt)
        return dt.isoformat()

    @classmethod
    def today_timestamp(cls, hour: int = 0, minute: int = 0, second: int = 0, microsecond: int = 0) -> float | None:
        return (
            datetime.today()
            .replace(hour=hour, minute=minute, second=second, microsecond=microsecond)
            .timestamp()
        )

    @classmethod
    def relative_timestamp(
        cls,
        datetime_from: datetime | float,
        days: int = 0,
        hours: int = 0,
        minutes: int = 0,
        seconds: int = 0,
        microseconds: int = 0,
    ) -> float | None:
        match datetime_from:
            case datetime():
                return (
                    datetime_from
                    + timedelta(
                        days=days,
                        hours=hours,
                        minutes=minutes,
                        seconds=seconds,
                        microseconds=microseconds,
                    )
                ).timestamp()
            case float():
                return (
                    datetime.fromtimestamp(datetime_from)
                    + timedelta(
                        days=days,
                        hours=hours,
                        minutes=minutes,
                        seconds=seconds,
                        microseconds=microseconds,
                    )
                ).timestamp()
            case _:
                return None

    @classmethod
    def epoch_converter(cls, epoch_time: datetime.timestamp):
        """
        Convert epoch time to human readable relative time.
        @param epoch_time: timestamp
        """
        current_epoch = int(datetime.now().timestamp())
        epoch_difference = current_epoch - epoch_time
        if epoch_difference <= 60:
            response = "now"
        elif 60 < epoch_difference <= 3600:
            response = "{} minutes ago".format(int(epoch_difference // 60))
        elif 3600 < epoch_difference <= 86400:
            response = "{} hours ago".format(int(epoch_difference // 3600))
        elif 86400 < epoch_difference <= 172800:
            response = "yesterday"
        else:
            response = "{}".format(
                datetime.fromtimestamp(epoch_time + 60 * 60 * 7).strftime(
                    "%d %b %Y %H:%M %p"
                )
            )
        return response

    @classmethod
    def parse_datetime_dynamic(cls, data) -> datetime | None:
        """
        If data is string, convert to datetime object use ISO format.
        If data is int, convert to datetime object use timestamp.
        """
        if data is None or isinstance(data, datetime):
            return data
        if isinstance(data, str):
            return datetime.fromisoformat(data)
        elif isinstance(data, (float, int)):
            return datetime.fromtimestamp(data)

    @classmethod
    def convert_iso_datetime_dynamic(cls, data) -> str | None:
        """
        If data is string or None, return.
        If data is datetime, convert to isoformat str.
        """
        if data is None or isinstance(data, str):
            return data
        if isinstance(data, datetime):
            return data.isoformat()

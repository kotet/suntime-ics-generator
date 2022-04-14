import argparse
from typing import List
from ics import Calendar, Event
from ics.alarm.custom import CustomAlarm,BaseAlarm
from datetime import datetime, timedelta
from suntime import Sun


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sunrise-name", type=str,
        help="name of sunrise events", default="日の出"
    )
    parser.add_argument(
        "--sunset-name", type=str,
        help="name of sunset events", default="日の入り"
    )
    parser.add_argument(
        "--alarm-dur-minutes", type=int,
        help="set alarm before n minutes of suntime", default=60
    )
    parser.add_argument(
        "--disable-sunrise", type=bool,
        default=False,
    )
    parser.add_argument(
        "--disable-sunset", type=bool,
        default=False,
    )
    parser.add_argument(
        "--disable-alarm", type=bool,
        default=False,
    )
    parser.add_argument(
        "--latitude", type=float, default=35.2815899 # nagoya, japan
    )
    parser.add_argument(
        "--longitude", type=float, default=137.0880719 # nagoya, japan
    )
    parser.add_argument(
        "--start-date-offset", type=int,
        default=-500
    )
    parser.add_argument(
        "--end-date-offset", type=int,
        default=500
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    s = Sun(args.latitude, args.longitude)
    c = Calendar()

    today = datetime.today()

    alarms: List[BaseAlarm] = []
    if not args.disable_alarm:
      alarms = [CustomAlarm(trigger=timedelta(minutes=args.alarm_dur_minutes))]

    for offset in range(args.start_date_offset, args.end_date_offset):
        date = today + timedelta(days=offset)

        if not args.disable_sunset:
            t = s.get_sunset_time(date)
            c.events.add(
                Event(
                    name=args.sunset_name,
                    begin=t,
                    end=t,
                    alarms=alarms
                )
            )
        
        if not args.disable_sunrise:
            t = s.get_sunrise_time(date)
            c.events.add(
                Event(
                    name=args.sunrise_name,
                    begin=t,
                    end=t,
                    alarms=alarms
                )
            )
    print(c)


if __name__ == "__main__":
    main()

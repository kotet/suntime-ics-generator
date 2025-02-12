# suntime-ics-generator

Example: http://kotet.jp/suntime-ics-generator/nagoya.ics

```
$ poetry run python generate-calendar.py --disable-sunset --sunset-name="SUNRISE" --latitude=35.6812405 --longitude=139.7649361 --start-date-offset=-100 --end-date-offset=300 > tokyo-sunrise.ics
```
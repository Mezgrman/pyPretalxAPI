"""
Copyright (C) 2023 Julian Metzler

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import datetime
import dateutil.parser


def max_duration_filter(event, hours, minutes):
    _time = datetime.datetime.strptime(event['duration'], "%H:%M").time()
    duration = datetime.timedelta(hours=_time.hour, minutes=_time.minute)
    return (duration <= datetime.timedelta(hours=hours, minutes=minutes))

def ongoing_or_future_filter(event, max_ongoing):
    now = datetime.datetime.now()
    start = dateutil.parser.isoparse(event['date']).replace(tzinfo=None)
    _time = datetime.datetime.strptime(event['duration'], "%H:%M").time()
    duration = datetime.timedelta(hours=_time.hour, minutes=_time.minute)
    now_start_delta = (now - start)
    return (now < start) or (now_start_delta.total_seconds() <= (max_ongoing * 60) and now_start_delta < duration)
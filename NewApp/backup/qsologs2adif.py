#!/usr/bin/env python3

import sys


header = """ADIF Export
<adif_ver:5>3.1.1
<created_timestamp:15>20210409 120831
<programid:6>WSJT-X
<programversion:9>2.4.0-rc4
<eoh>
"""

row_template = """<call:%d>%s <gridsquare:0> <mode:3>FT8 <rst_sent:%d>%s <rst_rcvd:%d>%s <qso_date:8>%s <time_on:6>%s <qso_date_off:8>%s <time_off:6>%s <band:3>%s <freq:9>%s <station_callsign:%d>%s <my_gridsquare:%s>%s <eor>"""

print(header)

previous_qso_date = 0
previous_qso_time = 0
previous_remote_callsign = ""

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        qso_frequency, qso_date, qso_time, qso_my_callsign, qso_remote_callsign, qso_rst_received, qso_rst_sent, qso_my_grid = line.split(",")
        qso_frequency = int(qso_frequency) / 1000000.0
        qso_rst_received = qso_rst_received.strip("R")
        qso_time = qso_time.replace(":", "") + "00"

        if abs(int(qso_time) - previous_qso_time) <= 100 and previous_qso_date == qso_date and previous_remote_callsign == qso_remote_callsign:
            previous_qso_time = int(qso_time)
            previous_qso_date = qso_date
            previous_remote_callsign = qso_remote_callsign
            continue
        previous_qso_time = int(qso_time)
        previous_qso_date = qso_date
        previous_remote_callsign = qso_remote_callsign

        f = float(qso_frequency)
        band = "XXX"
        if f > 7 and f < 7:
            band = "40m"
        elif f > 14 and f < 15:
            band = "20m"
        elif f > 18 and f < 19:
            band = "17m"
        elif f > 21 and f < 22:
            band = "15m"

        print(row_template % (len(qso_remote_callsign), qso_remote_callsign,
            len(qso_rst_sent), qso_rst_sent, len(qso_rst_received),
            qso_rst_received, qso_date, qso_time, qso_date, qso_time, band,
            qso_frequency, len(qso_my_callsign,), qso_my_callsign,
            len(qso_my_grid), qso_my_grid))

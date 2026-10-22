#!/usr/bin/env python3
"""Read-only DroneGuard MAVLink probe. Sends no vehicle-control commands."""
import argparse
import json
import time
from datetime import datetime, timezone

from pymavlink import mavutil


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--endpoint", default="udp:127.0.0.1:14540",
                        help="Local SITL MAVLink endpoint (default: %(default)s)")
    parser.add_argument("--seconds", type=float, default=8.0,
                        help="Probe duration; default 8 seconds")
    args = parser.parse_args()
    if args.seconds <= 0 or args.seconds > 60:
        parser.error("--seconds must be between 0 and 60")

    print(f"Connecting read-only to {args.endpoint} for {args.seconds:.1f}s")
    link = mavutil.mavlink_connection(args.endpoint, autoreconnect=False,
                                      source_system=255, source_component=190)
    deadline = time.monotonic() + args.seconds
    state = {"connected": False, "mode": None, "armed": None,
             "latitude": None, "longitude": None, "altitude_m": None,
             "groundspeed_m_s": None, "heading_deg": None,
             "battery_voltage_v": None, "battery_remaining_pct": None,
             "gps_fix_type": None, "last_message": None}
    while time.monotonic() < deadline:
        msg = link.recv_match(blocking=True, timeout=min(1.0, max(0.1, deadline-time.monotonic())))
        if msg is None:
            continue
        kind = msg.get_type()
        if kind == "BAD_DATA":
            continue
        state["connected"] = True
        state["last_message"] = kind
        if kind == "HEARTBEAT":
            state["armed"] = bool(msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED)
            state["mode"] = mavutil.mode_string_v10(msg)
        elif kind == "GLOBAL_POSITION_INT":
            state["latitude"] = msg.lat / 1e7
            state["longitude"] = msg.lon / 1e7
            state["altitude_m"] = msg.relative_alt / 1000.0
            state["heading_deg"] = None if msg.hdg == 65535 else msg.hdg / 100.0
        elif kind == "VFR_HUD":
            state["groundspeed_m_s"] = round(float(msg.groundspeed), 3)
        elif kind == "SYS_STATUS":
            state["battery_voltage_v"] = None if msg.voltage_battery == 65535 else msg.voltage_battery / 1000.0
            state["battery_remaining_pct"] = None if msg.battery_remaining < 0 else int(msg.battery_remaining)
        elif kind == "GPS_RAW_INT":
            state["gps_fix_type"] = int(msg.fix_type)
    state["observed_at_utc"] = datetime.now(timezone.utc).isoformat()
    print(json.dumps(state, indent=2))
    link.close()


if __name__ == "__main__":
    main()

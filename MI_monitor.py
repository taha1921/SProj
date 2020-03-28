import os
import sys
# Import MobileInsight modules
from mobile_insight.monitor import OnlineMonitor

if len(sys.argv) < 3:
        opt.error("please specify physical port name and baudrate.")
        sys.exit(1)

# Initialize a 3G/4G monitor
src = OnlineMonitor()
src.set_serial_port(sys.argv[1]) #the serial port to collect the traces
src.set_baudrate(int(sys.argv[2])) #the baudrate of the port

# Specify logs to be collected: (supported messages: http://www.mobileinsight.net/msg_type.html)
src.enable_log("LTE_RRC_OTA_Packet")
src.enable_log("WCDMA_RRC_OTA_Packet")

# Save the monitoring results as an offline log
src.save_log_as("./monitor-example.mi2log")

# Start the monitoring
src.run()
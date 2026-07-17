# Edge AI Lab Inventory

| Device | Hostname | IP | OS | Role | AI Runtime Target | Status |
|---|---|---|---|---|---|---|
| Laptop | laptop-dev-01 | 192.168.1.xx | Windows / Linux | Development + dashboard + analysis | PyTorch / GitHub / Docker | Active |
| Jetson Orin Nano Super | jetson-orin | 192.168.1.60 | JetPack / Ubuntu | Main GPU AI node | TensorRT / DeepStream / PyTorch CUDA | Active |
| Jetson Nano | jetson-nano | 192.168.1.61 | JetPack / Ubuntu | Secondary GPU AI node | TensorRT / PyTorch CUDA | Active |
| Raspberry Pi 5 | raspi5 | 192.168.1.62 | Raspberry Pi OS 64-bit | Main CPU AI node | ONNX Runtime / NCNN / OpenCV | Active |
| Raspberry Pi 4 | raspi4 | 192.168.1.63 | Raspberry Pi OS 64-bit | Services + monitoring node | MQTT / Node-RED / Prometheus / Grafana | Active |
| Raspberry Pi 3 | rpi3-light-01 | 192.168.1.xx | Raspberry Pi OS | Lightweight edge node | MQTT client / watchdog / telemetry | Active |
| ESP32 | esp32-sensor-01 | DHCP / static | Firmware | Sensor node | MQTT telemetry | Pending |
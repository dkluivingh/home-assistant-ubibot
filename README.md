# Ubibot integration for Home Assistant

This repo provides a plugin to work with Ubibot thermometers as sensors

## Installation

Install using HACS

## Configuration

Configure as a sensor in HA YAML configuration.yaml

api_key: = account key not sensor api key

```
sensor:
  platform: ubibot
  api_key: !secret ubibot_apikey
  channel: !secret ubibot_channel_number_1
  scan_interval: 900
```
```
sensor:
    - platform: ubibot
      account_key: ssdadasasd
      api_key: !secret ubibot_apikey
      channel: !secret ubibot_channel_number_1
      scan_interval: 900
    - platform: ubibot
      account_key: ssdadasasd
      api_key: !secret ubibot_apikey
      channel: !secret ubibot_channel_number_2
      scan_interval: 900
```

Store secrets in secrets.yaml

```
ubibot_apikey: "YOUR_API_KEY" 
ubibot_channel_number_1: "YOUR_CHANNEL_NUMBER"
```

```
ubibot_apikey: "YOUR_API_KEY" 
ubibot_channel_number_1: "YOUR_CHANNEL_NUMBER"
ubibot_channel_number_2: "YOUR_CHANNEL_NUMBER"
```

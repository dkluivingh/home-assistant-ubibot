"""Constants for Ubibot module."""
from homeassistant.const import (
    UnitOfTemperature,
)
from homeassistant.components.sensor import (
    SensorDeviceClass,
)

SENSOR_TYPES = {
    "temperature": {
        "class": SensorDeviceClass.TEMPERATURE,
        "unit": UnitOfTemperature.CELSIUS,
        "icon": "mdi:thermometer",
        "field": "field1",
    },
    "humidity": {
        "class": SensorDeviceClass.HUMIDITY,
        "unit": "%",
        "icon": "mdi:water-percent",
        "field": "field2",
    },
    "lux": {
        "class": SensorDeviceClass.ILLUMINANCE,
        "unit": "lx",
        "icon": "mdi:lightbulb-on-outline",
        "field": "field3",
    },
}

MODELS = {"ubibot-ws1": "WS1"}

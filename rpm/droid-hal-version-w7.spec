# rpm_device is the name of the ported device
%define rpm_device w7
# rpm_vendor is used in the rpm space
%define rpm_vendor lge
# Manufacturer and device name to be shown in UI
%define vendor_pretty LG
%define device_pretty Optimus L90
# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator 1
%define have_led 0
%include droid-hal-version/droid-hal-version.inc

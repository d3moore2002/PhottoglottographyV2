# Mechanical Placement Device for Photoelectroglottography

## Overview

This repository contains the mechanical design files for a custom 3D-printed placement device developed for a low-cost photoelectroglottography system. The device is designed to position an infrared light source and photodetector around the laryngeal region in a repeatable and stable way during voice and breathing measurements.

Photoelectroglottography is an optical measurement technique that detects changes in transmitted infrared light through the glottal region as the vocal folds open and close during phonation. Because the signal depends strongly on sensor placement, this mechanical housing was designed to improve alignment, reduce placement variability, and support consistent skin contact during testing.

## Purpose

The placement device was created to address a key challenge in optical throat sensing: maintaining a stable and repeatable position of the infrared emitter and detector during speech tasks.

The device is intended to:

- Hold the IR sensor in a fixed pocket over the laryngeal region
- Position IR light sources in a repeatable vertical housing
- Reduce noise caused by hand placement or inconsistent sensor alignment
- Improve comfort and stability during testing
- Support future wearable and wireless versions of the system

## Design Features

### Sensor Pocket

The front-facing base pocket is designed to hold the IR sensor module in a centered and repeatable position. This helps maintain consistent sensor-to-skin contact and reduces variability between trials.

### Vertical IR Light Housing

The vertical ladder-style housing is designed to route and position IR LEDs along the neck. This provides a controlled illumination path through the throat region while keeping the emitter placement consistent across tests.

### Curved Neck Geometry

The main body of the device follows a curved form to better fit the front of the neck. This improves ergonomics and helps the housing sit more naturally against the skin.

### Anatomical Shift

Initial design testing showed that a center-positioned sensor could interfere with the thyroid cartilage, also known as the Adam’s apple. To reduce this issue, the sensor position was shifted slightly to the right while maintaining the optical path between the IR source and detector.

### Ambient Light Shielding

The housing helps shield the sensor from ambient light, reducing optical noise and improving signal consistency.

## Intended Use

This device is intended for research and prototype testing of a photoelectroglottography-based voice measurement system. During testing, the device is placed against the throat while the user performs controlled vocal or breathing tasks.

Example testing tasks include:

- Glottal opening and closure
- Repeated vowel phonation
- Gasping
- “Uh-oh” phonation
- Tidal breathing

Photodiode voltage changes can then be measured as the vocal folds open and close.

## Applications

### Current Applications

- Linguistic research studies
- Measuring voiced and voiceless sound differences
- Measuring phonation types
- Estimating open quotient
- Cross-language phonetics research

### Future Applications

With further validation, this device could support:

- Vocal fold paralysis monitoring
- Laryngeal cyst or mass monitoring
- Muscle tension dysphonia studies
- Voice therapy and training for vocalists
- Wearable voice monitoring systems

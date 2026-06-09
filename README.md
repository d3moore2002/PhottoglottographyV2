# Measuring the Larynx Using Light, A Low-Cost Photoelectroglottography Tool (Prototype)
## UC San Diego Bioengineering Capstone: 2025-26.

### Mentors: Will Styler, Marc Garellek
### Team 5: Donovan Moore (drmoore.dm2002@gmail.com), Isaiah Mitchell (), Amir Hojaiji ()

Previous Acknowledgement: Thank you Deepta, Vaughan, Erica, and Isabelle for your work! https://github.com/dz-enigmatologist/Photoglottography

## Problem Statement
There is a need for a non-invasive, low-cost instrument capable of reliably recognizing changes in laryngeal aperture during speech in a research and in future iterations, perhaps a medical setting. 

## Overview of Solution
We designed an external photoelectroglottography tool. A 850 nm infrared (IR) LED was positioned superior to the thyroid cartilage (Adam’s apple), allowing light to pass through the glottal and vocal fold cross-sectional area, where the diffused light was detected using a BPW34 photodiode sensor placed at the suprasternal notch to indirectly measure stages of vocal fold abduction and adduction. The photodiode outputs a reverse current, proportional to the exposed light and converted this current into a voltage using an LTC6268 trans-impedance amplifier circuit. Using an Arduino Uno, the voltage signal can be visualized in Arduino IDE, and then digitized as a list of .csv values for post-processing analysis in python. 

To evaluate the efficacy of the device, project members and the faculty advisor performed phonatory tasks including glottal stops, tidal breathing, and sustained vowels at varying pitches. Initial testing demonstrated that the device could distinguish between these vocal behaviors under limited experimental conditions within a dark room. With proof of concept established, future work will focus on transitioning the current prototype into a more refined design while improving signal quality, noise reduction, and overall system robustness.

### Subprojects and Contributions
- Circuit Design (Donovan and Isaiah)
- Signal Acquisition and Processing (Donovan) 
- Mechanical Placement Holder (Amir)

### Project Components and Ovverview
Experimental Setup
Circuit Design

### Documentation
[Component_Datasheets](Component_Datasheets/)

[Circuit Schematics](Circuit_Schematics/)

### Github Contributions 
- Repository creation and template - Donovan

## Our Team!
<img width="2048" height="1536" alt="image" src="https://github.com/user-attachments/assets/fe6a1e17-00a2-4866-9eb4-eb4958522cad" />

## Bionegineering Day 2026 Poster
<img width="2500" height="1875" alt="05Poster pdf pptx" src="https://github.com/user-attachments/assets/af42015a-a891-492c-8a1c-16a1ebd87467" />

















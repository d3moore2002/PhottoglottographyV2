# Measuring the Larynx Using Light, A Low-Cost Photoelectroglottography Tool (Prototype)
## UC San Diego Bioengineering Capstone: 2025-26.

### Mentors: Will Styler, Marc Garellek
### Team 5: Donovan Moore (drmoore.dm2002@gmail.com), Isaiah Mitchell (), Amir Hojaiji ()

## Problem Statement
There is a need for a non-invasive, low-cost instrument capable of reliably recognizing changes in laryngeal aperture during speech in a research and in future iterations, perhaps a medical setting. 

## Overview of Solution
We designed an external photoelectroglottography tool. A 850 nm infrared (IR) LED was positioned superior to the thyroid cartilage (Adam’s apple), allowing light to pass through the glottal and vocal fold cross-sectional area, where the diffused light was detected using a BPW34 photodiode sensor placed at the suprasternal notch to indirectly measure stages of vocal fold abduction and adduction. The photodiode outputs a reverse current, proportional to the exposed light and converted this current into a voltage using an LTC6268 trans-impedance amplifier circuit. Using an Arduino Uno, the voltage signal can be visualized in Arduino IDE, and then digitized as a list of .csv values for post-processing analysis in python. 

To evaluate the efficacy of the device, project members and the faculty advisor performed phonatory tasks including glottal stops, tidal breathing, and sustained vowels at varying pitches. Initial testing demonstrated that the device could distinguish between these vocal behaviors under limited experimental conditions within a dark room. With proof of concept established, future work will focus on transitioning the current prototype into a more refined design while improving signal quality, noise reduction, and overall system robustness.

### Subprojects and Contributions
- Circuit Design (Donovan and Isaiah)
- Signal Acquisition and Processing (Donovan) 
- Mechanical Placement Holder (Amir)

### Project Video
https://youtu.be/zr6Eg0ug8D4

### Project Components and Ovverview
[Project Background](Project_Background/README.md)

[Experimental Setup](Experimental_Setup/README.md)

[Circuit Design](Circuit_Design/README.md)

[Mechanical Placement Design](Mechancial_Placement_Device/README.md)

[Data Acquisition and Processing](Data_Acquisition_and_Processing/README.md)

### Documentation
[Component_Datasheets](Component_Datasheets/)

[Timeline/Budget/Appendix](Additional_Documents/)

[References](References/)

### Github Contributions 
##### Donovan 
###### Repository Template, organization, and README
####### Circuit Design
####### Data Acquisition and Processing

## Our Team!
<img width="2048" height="1536" alt="image" src="https://github.com/user-attachments/assets/fe6a1e17-00a2-4866-9eb4-eb4958522cad" />

## Bionegineering Day 2026 Poster
<img width="2500" height="1875" alt="05Poster pdf pptx" src="https://github.com/user-attachments/assets/af42015a-a891-492c-8a1c-16a1ebd87467" />

## Conclusion 
As stated in Section 5 our primary goal was to achieve a high quality signal for ePGG measurements. Throughout the process of developing new iterations of the circuit and making necessary changes to adjust for bottlenecks, such as signal to noise ratio, we were successful in achieving this signal. In order to address the previously stated bottlenecks we removed the LM358 secondary op-amp leaving just the transimpedance amplifier to adjust the sensitivity of our infrared sensor. This change allowed us to achieve the minimum of distinguishing between the different glottal phases: tidal breathing, glottal stops, and glottal opening. For our second goal we focused on enabling consistent quantification of glottal motion across users. The bottlenecks that we encountered while pursuing this goal include darker skin tones, thicker necks, anatomical differences, and most importantly having a limited testing pool. The issue of the limited testing pool and our prioritization of goals 1 and 3 held us back from being able to fully achieve this goal. However, we were able to address the majority of the bottlenecks through adjusting the power of the LED and obtaining reliable results when testing on Donovan, who is dark skin, Isaiah, who is dark skin with a more prominent Adam's apple, and Will, our mentor who has light skin and a thicker neck. The next step to achieve this goal is to expand the testing pool and test how the device works on women to ensure consistent results regardless of anatomical differences, as women have a less prominent Adam’s Apple than men. Our final goal was to optimize sensor and light source placement to improve measurement accuracy and precision. During testing, we discovered the issues of the device’s sensitivity to muscle movement and directionality of the LED. For this goal we were able to confirm a general placement that would allow us to capture the signal that would work on most people, where the sensor is placed on top of the collar bone aligning with the trachea and the LED is placed in the crook of the neck under the jaw. In the case of our evaluation we were successful in achieving this goal, but the next step in fully achieving this goal would be to test with a more improved placement device that can adjust vertically for differing neck lengths rather than laterally for different widths.

## Limitations 
The electrical circuit demonstrated the necessary qualifications for our PI to deem as a working device, but there could be some improvements such as adding a potentiometer and transferring the design to a PCB. These improvements would address current limitations that are presented in testing such as loose wiring and maintaining consistency for anatomical differences. The general limitations of the device is that even with the knowledge of appropriate placement the device is still prone to muscle movement, and the direction of light from the LED is not currently measurable. Another limitation that needs to be addressed is that the transistor in the circuit is prone to heating up leading to potential short circuits. The data acquisition allows us to capture reliable data of glottal phases with a limitation of frequency errors in analyzing the data which could be solved by implementing a lock-in amplifier for preprocessing to keep the readings consistent and contribute to checking for noise.

## Improvements
Electrical Improvements:
Improvements that can be made to help improve the accuracy and reliability of the circuit include adding potentiometers, heat sinks, and a lock-in amplifier. The potentiometers would help scientists to adjust the power the LED emits as needed to accommodate for the different physiology and anatomy of the users of the device. The heat sinks would help ensure that the circuit does not short circuit and allows for more consistent and longer uses of the device during testing, while also improving the safety and accessibility of the device. The lock-in amplifier would help with enhancing our current method of data acquisition allowing future teams and users to keep the frequency at a consistent rate that is easy to analyze for processing. Furthermore, with the improvements implemented, future teams can gather more information on the comparisons between our ePGG and other methods of identifying different phonations.

Integration with Acoustic Data
The usefulness of the glottogram signal increases significantly when it is analyzed alongside acoustic recordings of speech. By recording both glottal motion and audio output simultaneously, researchers can compare the physical behavior of the vocal folds with the sounds produced during speech. This combined analysis can provide valuable insights for both linguistic research and clinical voice assessment. Similar glottal movement patterns may produce different acoustic outputs, and analyzing both signals together helps provide a more complete understanding of vocal production.

### Acknowledgements
2024-25 Team: Thank you Deepta, Vaughan, Erica, and Isabelle for your work establishing the project for it to become senior design! https://github.com/dz-enigmatologist/Photoglottography

Thank you to our mentors Dr. Will Styler and Dr. Marc Garellek for their wisdom and oversight!

Thank you Dr. Taylor, Iris, and Yashwin for oversight and grading throughout the senior design process!

















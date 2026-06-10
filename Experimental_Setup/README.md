## Testing Methodology
To begin testing, the circuit must be powered using the appropriate voltage supplies. For the light circuit, this is especially key, as the light will turn on, but not propagate through tissue well without enough power. In our current setup, every component on the breadboard is prewired besides the LED(s), photodiode, power supplies, and signal to the Arduino analog pin. Hence, these components need to be plugged into the appropriate places in the setup. Although the current setup requires manual wiring of the sensors and power supplies, future iterations of the system aim to simplify the electrical connections and improve usability for researchers with varying technical backgrounds.

## Vocalization Test Conditions
After device setup and placement of LED and sensor, testing requires controlled vocalization to evaluate whether the device can detect changes in glottal aperture. Several phonetic sounds were used to test the device under different glottal conditions. Saying /uh/ – represents a glottal stop and is expected to produce light blockage, /oh/ – represents sustained vocal fold vibration with partial glottal opening and closing, /sigh/ – represents an open glottal configuration that should allow more light transmission, tidal breathing represents a sinusoidal life waveform with a periodicity based on your rate of breathing, and sustained vowels such as /aaa/, /ooo/, /eee/, represented by small by rapid oscillations in the signal associated with the rapid vocal fold vibration. By varying the speed and duration of these vocalizations, it should be possible to observe changes in the detected optical signal. 

## Experimental Procedures
The following procedure was used during device testing:
Connect the BPW34 photodiode to the circuit.
Connect the infrared LED emitters to the illumination circuit.
Connect the output of the LTC6268 op-amp to the Arduino analog input pin.
Power the operational amplifiers and transistor circuits using the appropriate power supplies.
Connect the Arduino Uno to a computer via USB.
Open the Arduino Serial Plotter to visualize the incoming signal.
Perform a basic sensor test by blocking the photodiode with a hand or skin to verify that the signal responds to changes in light intensity.
Position the photodiode and LED emitters around the laryngeal region near the Adam’s apple using the placement device or manual positioning.
Perform controlled vocalizations such as tidal breathing, glottal opening, and glottal closure.
Once properly positioned determined through these tests, run python code, close Arduino IDE and keep the Arduino plugged in via USB. 
Voice while python code runs, the raw analog readings from the Arduino Uno will be plotted in a .csv file over time. The .csv file should save automatically to the folder after the acquisition code finishes in the allocated time set via code (though for now, it's put to 60 seconds)
Take the .csv file, and use Matplotlib to visualize the signal.

## Results
Signal Characteristics
Figure 35: Photoelectroglottgraphy data measured over a 1 minute time frame from voicing. Data was sampled directly from the Arduino analog A0 pin at 500 Hz and the serial monitor values were saved as a .csv file, where it was visualized and analyzed in a Python Jupyter notebook.



Region I: Glottal Stops (5 to 15 seconds)
	The device successfully distinguished five glottal stops performed within the time period, with the voltage drops being a positive sign. In the graph we see 5 distinct drops in voltage reading, indicating there is a brief closure in the vocal folds to block potential IR light from reaching the photodiode sensor. However, there is a minor concern with the accuracy of the signal. Glottal stops may cause the entire larynx to shift downwards due to thyroid cartilage movement, which can alter the position of the IR LED light(s) or photodiode sensor. This can create a muscle artifact, interrupting the efficacy of our glottogram signal, which is a concern mentioned in more depth in the background section. 

Region II: Tidal breathing (18 to 32 seconds) 
	The device successfully identified the performance of tidal breathing, with three moderate deep breaths with inhales and exhales for each complete cycle. This result is significant, as this vocalization does not shift the entire larynx. One major concern with the device as identified in the background is due to thyroid cartilage tendency to shift while speaking. Tidal breathing however does not result in as much abrupt muscular activity that shifts the cartilage around the electrical components, increasing the likelihood of the device being at least partially successful in measuring this particular stage of glottal aperture and that this proof of concept is possible.

Region III: Sustained vowels (/aaaa/) (35 to 55 seconds)
	While there are distinct voltage shifts between the different stages of sustained vowel voicing, it is uncertain if these changes are truly a measurement of the vocal fold activity in the larynx or closer to a muscle artifact or external light acting as a potential source of noise. The sustained vowels were done at various pitches, a “normal”, then “deep” then “high” pitch. For us, it is not entirely clear what differences would be monitored with voicing at different pitches. If the device is tested on more individuals and additional literature reviews are performed, the future team can obtain a better idea of what to expect from this specific test.

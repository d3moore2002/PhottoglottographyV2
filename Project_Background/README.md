**Brief Overview of the Larynx**

The larynx, otherwise known as your voice box has 3 essential functions, to protect the lower respiratory tract, swallow food, and produce sound through phonation. [5,6] Phonation is the process of how the larynx produces sound, when airflow from the lungs cause vibration of the folds. The larynx is encompassed by an intricate system of largeneyal muscles and cartilage that holds the structure in place and performs necessary movement. Anatomically, the larynx is about 4 cm to 5 cm in height, and located in the neck around the C3 to C7 section of the vertebrae. Men have larger larynxes on average than women, which correlates to men having deeper voices and a more visible laryngeal prominence, otherwise known as the Adam’s Apple. [5]

**Vocal Folds Role of the Larynx**

The larynx is split into three regions, the subglottis, glottis, and supraglottis, orientated from bottom to top. The site where phonation occurs is at the glottis region where the vocal folds, glottis, and larynx ventricles are located. [6] The true vocal folds (otherwise known as “vocal cords”) are structures of layered tissue that open, close and vibrate during speech. Though the term “vocal cords” are more commonly used, vocal folds more accurately reflect their muscular design and folding motion during vibration. Airflow from the lungs causes the vocal folds to oscillate and produce a periodic sound wave that can be measured in an ePGG system. [5,6]. The vestibular vocal folds lie on top of true vocal folds whose primary function is to protect the airway and assist in swallowing, and do not have a known role in normal speech production.  Our device wants to measure the laregenal activity in the glottal region, where the and measure the opening, closing, and vibration of the “true” vocal folds. 

<img width="240" height="200" alt="Screenshot 2026-06-09 at 7 44 02 PM" src="https://github.com/user-attachments/assets/578ffef0-26df-42fb-8868-14b9a6194e77" />

Figure 1: Anatomy of the Larynx. Laryngoscopic view showing the interior structures of the larynx, including the vallecula, epiglottis, tubercle of the epiglottis, vocal fold, ventricular fold, aryepiglottic fold, cuneiform cartilage, corniculate cartilage, and trachea. [5]

**Musculature of the Larynx**

The larynx has many muscles that control vocal position and tension while breathing, speaking and swallowing. These muscles are intrinsic laryngeal muscles because they are primarily involved within the inner functions of the larynx. [5] In respiration, the vocal folds abduct (move away from midline) to allow air to pass through the airway, which is performed by the posterior cricothyroid muscles. [5]. During phonation the vocal folds adduct (move toward the midline) and this produces the highest sound quality, which is performed by a few different muscles at once, the thyroarytenoid, interarytenoid, and the lateral cricoarytenoid. [5] Pitch modulation occurs where there is changes in vocal fold tension through a change in their position or length. 

**Cartilage of the Larynx**

The cartilage of the larynx is what enables it to have a flexible but secure physiological structure. [6] The most prominent is the thyroid cartilage, as the two lamine of them join together to form the Adam’s apple. The position of the Adam’s apple can act as an external landmark for estimating the place of the vocal folds, which is slightly inferior to this point. [5,6] The hyoid bone, which is located superior to the larynx, connects it to the jaw and surrounding musculature. As a result, large jaw and tongue movements can manipulate the position of the whole larynx [5,6], introducing a signal artifact to our system. For example, while swallowing the larynx elevates upward to protect the airway. Placement of the sensor in this area while swallowing may give a potential false signal due to the changes in skin tension from the larynx shifting. Additionally, cartilage itself influences how light propagates through biological tissue, which can cause scattering or attenuation of the optical signal. Due to the physiological complexity of the larynx and the amount of cartilage structures that exist around the region, indirect methods of monitoring largenal performance, particularly during speech, can be difficult, and must be considered within our design. 

<img width="274" height="319" alt="Screenshot 2026-06-09 at 7 44 48 PM" src="https://github.com/user-attachments/assets/acae3f65-2264-4a29-856a-107a68fd8225" />

Figure 2: The Larynx, Ligaments of the larynx; Posterior view, Cartilago triticea, Hyothyroid membrane, Corniculate cartilage, Arytenoid, Posterior cricoarytenoid ligament, Cricothyroid articulation Henry Vandyke Carter, Public Domain, via Wikimedia Commons [6]

**Electrophotoglottograpy**

ePGG is a measurement technique that uses optical sensing and electronic signal processing to monitor vocal fold motion during phonation. The term can be decomposed into three functional components of the measurement system: optical sensing, electrical signal acquisition, and signal processing. 

First, the device uses optical sensing to measure vocal fold adduction and abduction during speech. Light emitted from a source interacts with the true vocal folds within the glottal region, and variations in the geometry of the true vocal folds during phonation alter the amount of transmitted and scattered light detected by a photodetector. These changes in detected light intensity correspond to changes in the glottal opening and can therefore be used as an indirect measurement of vocal fold movement.  

Second, the detected optical signal must be converted into a measurable electrical signal. A photodetector converts incoming light into a small photocurrent, which is then amplified and conditioned through an analog circuit to produce a readable voltage signal. 

Third, the resulting electrical signal is acquired and processed to quantify vocal fold activity. Signal processing techniques can be used to extract relevant features such as amplitude variations and temporal patterns, enabling analysis of vocal fold performance during speech. 

**Key Technologies**

Photodiodes are semiconductor devices designed to convert incident light into electrical current. When photons strike the photodiode’s semiconductor junction, they generate electron hole pairs that produce a small photocurrent proportional to the intensity of the incoming light.

Light Emitting Diodes (LEDs) are semiconductor devices that emit light when electrical current passes through a p–n junction. Infrared LEDs are used as the light can penetrate biological tissue more effectively than visible light.

Op-Amps are integrated circuits designed to amplify voltage signals. An ideal op-amp has extremely high gain, high input impedance, and low output impedance, making it useful for a wide range of analog signal processing applications.

Transimpedance amplifiers convert the small current generated by a photodiode into a measurable voltage signal. Because photodiodes produce current rather than voltage, direct measurement of the signal is difficult without this conversion stage.

Analog-to-Digital Converters (ADCs) are electronic components that convert continuous analog voltage signals into discrete digital values that can be processed by a computer or microcontroller.

**Electroglottography (EGG) Systems**

Electroglottography (EGG) is one of the most commonly used non-invasive techniques for monitoring vocal fold activity. In EGG systems, a pair of electrodes is placed on either side of the larynx on the surface of the neck. A small electrical current is passed between the electrodes, and changes in electrical impedance are measured as the vocal folds vibrate. Since biological tissues conduct electricity, impedance decreases when the vocal folds come into contact during phonation. As a result, the EGG signal provides useful information about vocal fold contact area during the glottal cycle, particularly during the closed phase of vocal fold vibration. However, EGG has notable limitations. Once the vocal folds separate during the open phase of the glottal cycle, the impedance measurement becomes less informative. Consequently, EGG signals provide limited insight into vocal fold behavior during the open phase of vibration. Additionally, commercial EGG systems are often expensive, and may be difficult for smaller research laboratories to obtain, thus, making them a useful, but inaccessible tool.

<img width="324" height="110" alt="Screenshot 2026-06-09 at 7 56 58 PM" src="https://github.com/user-attachments/assets/858189fc-8efe-485d-af30-25907ac5b056" />

Figure 3: Visual Electroglottography setup

**Photoelectroglottography (PGG) Systems**

Photoelectroglottography (PGG) is an optical method for analyzing glottal activity in which light is used to detect changes in the glottal opening during phonation. In early implementations of PGG, optical measurements were performed using fiber-optic endoscopes positioned near the glottis. These systems allowed researchers to simultaneously capture both images of the vocal folds and a corresponding glottographic waveform representing glottal activity. Despite their usefulness in research settings, fiber-optic PGG systems share many of the same limitations as other endoscopic approaches. They require specialized equipment, must be operated by trained professionals, and are invasive for subjects attempting to produce natural speech.

<img width="270" height="201" alt="Screenshot 2026-06-09 at 7 58 04 PM" src="https://github.com/user-attachments/assets/98cd2c47-b393-4017-9882-db873532346e" />

Figure 4: Supraglottal Illumination for a Photoglottography setup

# High-density intracranial recordings reveal a distinct site in anterior dorsal precentral cortex that tracks perceived speech
Repository contains code for the results described in the paper

Here we investigated high-density intracranial responses to speech in a feature film. Our focus was on the dorsal (pre)motor cortex, defined here as the dorsal part of the precentral gyrus and its surrounding areas with similar functional response. First, we showed that dorsal precentral cortex (dPCC) exhibited preference to speech over other tested sounds. Second, it was involved in tracking of speech auditory properties including speech spectral envelope, its rhythmic phrasal pattern and pitch contour. Third, it showed the ability to filter out noise from the perceived speech. Comparing these results to data from motor experiments showed that the identified region had a distinct location in dPCC, anterior to the hand motor area and superior to the mouth articulator region. Finally, we observed that the present findings were prominent in high-density intracranial data (~1mm electrode diameter, ~3mm inter-electrode distance) and lessened in subjects implanted with standard-density electrodes (~2mm electrode diameter, ~10mm inter-electrode distance).


![Alt text](/git_front.png?raw=true "Main results")


### The repository contains code for
 
- some control analyses on the audio
- t-test on average high frequency band (HFB) neural responses in dPCC to speech vs non-speech fragments
- cross-correlation of dPCC HFB to the spectral envelope of sound
- cross-correlation between HFB in the audiotory and motor (dPCC) cortices
- cross-correlation of dPCC HFB to the noisy speech fragments in the mixed soundtrack (the one patients actually heard) and the speech-only track (obtained from the movie company)
- linear fit of dPCC HFB to the phrasal groupings in speech (On/Of speech structure)
- partial correlation between HFB, sound spectral envelope and pitch
- comparison of modeling dPCC HFB using various audio properties during speech vs non-speech fragments
- control analyses using motor regressors (hand annotations)

Dependencies:
- [Numpy](https://numpy.org/)
- [Scipy](https://www.scipy.org/)
- [Scikit-learn](https://scikit-learn.org/)
- [Statsmodels](https://www.statsmodels.org/)
- [Scikit posthocs](https://github.com/maximtrp/scikit-posthocs)
- [Pympi](https://github.com/dopefishh/pympi)

Written in Python 3.7


### Data availability

The neural data supporting the current study are not shared here due to the restrictions on public sharing of the patients’ data. However it is possible to arrange access to the data through a data transfer agreement between research institutions. Interested parties can contact us [here](http://www.nick-ramsey.eu/contact/).


### About us

This work was done at the BCI lab of the University Medical Center in Utrecht. For more information please visit us at:
- [our github account](https://github.com/UMCU-RIBS)
- [our website](http://www.nick-ramsey.eu)


# Shreddit

## **Overview:**

* Shreddit is a web app designed to help musicians explore the chords, scales and the relationships between the two.

* Users can view scale and chord patterns in any key on a variety of stringed instruments and piano and hear audio samples of scales and chords.

* Users can chain together chord/scale pairs into progressions and Shreddit will generate a jam track that can be used to practice improvising with the selected combinations.

* Shreddit employs Teoria.js for music theory calculations and Tone.js for audio playback. Instrument displays and markers are all acheived with vanilla Javascript.

___

## **Functionality:**

Users will create a profile that will save their chord progressions.

Shreddit consists of three sections:

1. ### **Scale visualization:**

    * User-selected scale patterns are displayed on the instrument of their choice. User can select from different tunings of instruments and the key in which they want to view the scale.

    * Scale tones are represented by different colors relative to the tone's position in the scale. This helps to differentiate different patterns and arpeggios.

    * Users can playback the ascending and descending scale for reference.

2. ### **Chord visualization:**

    * This section is essentially the same as the scales section with chords. User can select chord names and the a key to view chord patterns on their selected instrument.

    * Audio playback of chords is available.

3. ### **Chord progression builder:**

    * When a user selects a chord, a list of scales that contain the chord tones is generated. The user can select a scale they want to use to improvise over that chord and create a pairing.

    * Pairings are linked together and compiled into a list. Users can then select a rhythm track and playback their chords over the rhythm. As the chords change, the respective paired scale will be represented on the instrument display.

    * Progressions can be saved to the user's profile, recalled later and shared with other users.

    * The progression builder will use selected chord changes to generate a list of popular songs that use those changes.

___

## **Data model:**

### **Users:**

The User model will contian:

* Basic user information: username, password, email, etc.

* A list of progressions they've saved and those shared with them.

### **Progression:**

The Progession model will contain:

* Title

* Progression Object:

  * *Chords:*  represented by arrays of notes.

  * *Durations:* How long each chord should be played.

  * *Velocities:* How hard each chord is hit.

The Progression object will be zipped together into chord/duration/velocity objects, which will be fed into a Tone.js loop which will playback the chords for the given durations at the desired velocity.

### **Future features:**

* Groups of progressions to make songs parts. Verse, chorus, bridge, etc.
* Generate sheet music or tabs from progressions
* Step sequencer for more customizable rhythms
* Chord progression flowchart based on probability of sequential chords or key modulations
* Step-by-step music lessons
* Faders to adjust playback instrument's voice
* Audio effects

### ***Timeframe:***

1. **December 20th:**
    * Scales and chords can be displayed on any selected instrument (hopefully piano, too) in any selected key.

    * Scale tones 1-12 will be marked individually with unique colors.

2. **January 2nd:**
    * User and Progression models will be setup as well as basic chord and rhythm playback.

    * Users will be able to create Progressions and save them to their profile.

3. **January 15th:**
    * Audio playback will be more developed.

    * Instrument display will change to represent the user's selected scale for each chord in their progression.

    * Hopefully instrument samples will be added to make the audio more realistic and not just sine and sawtooth waves playing chords and beats, though

4. ***February 7th:***
    * Add HookTheory API to generate a list of popular songs containing each set of chord changes.
    * Audio playback will be more defined. If, for some reason, I'm way ahead of schedule, I'm going to try to add a step sequencer for each a handful of drum samples so users can define their own beats, within reason. I would also like to add functionality for different parts in the audio loop (i.e. verse/chorus, variations on chord/scale combos).

### ***Resources:***

* Tone.JS - <https://tonejs.github.io/>

* Instrument samples with Tone.JS - <https://github.com/nbrosowsky/tonejs-instruments>

* Play chords with Tone.JS - <http://www.guitarland.com/MusicTheoryWithToneJS/PlayChords.html>

* Hook Theory: API for finding chord progressions in songs: <https://www.hooktheory.com/api/trends/docs>

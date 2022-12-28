A diode (continuity diode) is used here to protect the circuit. The cathode is the end with the silver ribbon connected to the power supply, and the anode is connected to the transistor.

When the voltage input changes from High (5V) to Low (0V), the transistor changes from saturation (amplification, saturation, and cutoff) to cutoff, and there is suddenly no way for current to flow through the coil.

At this point, if this freewheeling diode does not exist, the coil will produce a self-induced electric potential at both ends that is several times higher than the supply voltage, and this voltage plus the voltage from the transistor power supply is enough to burn it.

After adding the diode, the coil and the diode instantly form a new circuit powered by the energy stored in the coil to discharge, thus avoiding the excessive voltage will damage devices such as transistors on the circuit.

[Diode](https://docs.sunfounder.com/projects/euler-kit/en/latest/component/component_diode.html#cpn-diode)
[Flyback Diode](https://en.wikipedia.org/wiki/Flyback_diode)

At this point the program is ready to run, and after running you will hear the “tik tok” sound, which is the sound of the contactor coil inside the relay sucking and breaking.

Then we connect the two ends of the load circuit to pins 3 and 6 of the relay respectively.

..(Take the simple circuit powered by the breadboard power module described in the previous article as an example.)
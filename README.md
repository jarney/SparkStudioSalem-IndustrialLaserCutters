# Industrial 6090 150Watt CO2 Laser Cutters

This repository collects information about the Industrial
scale CO2 laser cutters at Spark Studios including
policies, safety information, training materials and technical
information such as wiring diagrams.

# Policies and procedures

This section covers the policies and procedures for operating the machines.

* Use of these machines is governed by the [Policies](policies.pdf).
* When running jobs, please follow the [Operations Checklist](operation-checklist.pdf)
* When running jobs, please fill out a sheet in the [Operation Log](operation-log.pdf)
* To achieve better surface finishes, please refer to the [Pro Tips](pro-tips.pdf)
* These Signs should be placed on the machines in event of malfunction to alert
  other users and Spark Studio board members of malfunctions.

If you wish th revise the policies, please edit the corresponding
OpenOffice (.odt) files and review with the Spark Studio Board.

# Technical Information

This section contains technical information for maintenance and
diagnosis of problems.  These are indended only for those tasked
specifically with maintaining and repairing the machines.  These
should not be used during normal operation.

This [operation manual](Gweike-operation-manual.pdf) covers
the use and operation of a similar laser cutter from Gweike.
While the laser cutters are not exactly this model, they
do give useful guidance on the machines and their operation.

The 6090 laser cutters are built using a Ruida controller
which interprets the GCode to guide the machine through making
cuts.  The [Ruida controller's documentation](RDC6445G-Control-System-V1.2-Manual.pdf)
describes more about its design and usage.

In addition, the [laser power supply has accompanying documentation](LASERPOWERSUPPLY欧规_1729590679720.pdf)
about its inputs and controls.

This [wiring diagram](laser-block-diagram.pdf) is
available for helping to understand the design of the
machines and general troubleshooting.  This diagram was produced
by reverse-engineering the design and is not authoritative,
but is as accurate as possible a diagram describing the wiring
of the machine based on its current configuration which has
been slightly altered from its original design.  The diagram is
authored in KiCad and future changes should be proposed and updated
using this format, reviewed, and implemented with the consent of
a Certifier or the Spark Studio Board.

# Modified Parts

Some parts have been designed and 3d printed in an effort to
improve the safety of the equipment.  These include:

* Spacers/stand-offs to hold a panel to prevent laser light from coming
  through the vent holes.
  
* Plugs for circular holes in front of Blue laser cutter.

* Holder for reed switch protecting the laser from firing with
  the door open.

The CAD for these files are maintained in this [FreeCAD file](LaserCutterParts.FCStd).

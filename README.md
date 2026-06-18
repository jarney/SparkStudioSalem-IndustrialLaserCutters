# Industrial 6090 150Watt CO2 Laser Cutters

This repository collects information about the Industrial
scale CO2 laser cutters at Spark Studios including
policies, safety information, training materials and technical
information such as wiring diagrams.

# Training Presentations
If you want to learn how to use the machines, there are several
presentations aimed at getting people started and certified:
* [Introduction Training](Training-GeneralPublic.pdf) and [handouts](Training-GeneralPublic-Handout.pdf): This course is intended for the general public
  to use the machines UNDER SUPERVISION of authorized users.  The nominal cost
  for this training is a $20 donation to the club.  You will learn to use the
  machine for basic cutting and engraving operations.  This is an introduction, so you
  will learn how to use the machines, but you will not yet be an expert.  This course makes use
  of some [templates](templates/svg) and a [template customization tool](https://jarney.github.io/spark/laser-cutters-6090/svg-templates/) to create
  designs for cutting during the class.

* [Authorized User Training](Training-AuthorizedUsers.pdf): This course is intended for paying members.  You will
  increase your knowledge and the focus is on ensuring safe operation and reacting to emergency
  conditions.  You will be allowed to use the machines unsupervised.

* Certifier Training (coming soon):  This course is intended for advanced users.  You will learn
  about the machine internals, alignment procedures, and more advanced topics.

# Policies and procedures

This section covers the policies and procedures for operating the machines.

* Use of these machines is governed by the [Policies](policies.pdf).
* When running jobs, please follow the [Operations Checklist](operation-checklist.pdf)
* When running jobs, please fill out a sheet in the [Operation Log](operation-log.pdf)
* Different materials should be cut and engraved with various settings.  While you may
  need to experiment to get the best results, the [Feeds and Speeds](FeedsAndSpeeds.pdf) document
  gives good starting points for common materials.
* To achieve better surface finishes, please refer to the [Pro Tips](pro-tips.pdf)
* These [Signs](signs.pdf) should be placed on the machines in event of malfunction to alert
  other users and Spark Studio board members of malfunctions.

If you wish to revise the policies, please edit the corresponding
OpenOffice (.odt) files and review with the Spark Studio Board.
Once approved, a pull-request can be sent to request that the official
copies of the policies be updated.  Note when revising policies, the
revision number and date MUST be updated in order to keep track
of which policy revision is the most recent.

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

# Modified Parts and accessories

Some parts have been designed and 3d printed in an effort to
improve the safety of the equipment.  These include:

* Spacers/stand-offs to hold a panel to prevent laser light from coming
  through the vent holes.
  
* Plugs for circular holes in front of Blue laser cutter.

* Holder for reed switch protecting the laser from firing with
  the door open.

The CAD for these files are maintained in this [FreeCAD file](LaserCutterParts.FCStd)
and printable versions can be found in the [STL](stl/) and [3MF](3mf/) directories.

# Alignment Procedures

The performance of the machines is highly dependent on how well
the machine is aligned.  Specifically, the optics must be aligned
closely with the gantry and the gantry needs to be square and parallel to
the bed.  Alignment of the machine is something of an art, but the
procedures are roughly outlined in the [Laser Alignment Guide](LaserAlignmentGuide.pdf).
These alignment procedures make use of some 3d-printed targets and
a [Laser Beam Alignment Worksheet](LaserBeamAlignmentWorksheet.svg) to assist in visualizing the beam path
and adjustments needed to bring the beam into the correct orientation.

There are beam target fixtures that can be inserted into the
apertures of [Mirror #2](stl/LaserCutterParts-P_AlignmentTarget_Mirror2.stl)
and [Mirror #3](stl/LaserCutterParts-P_AlignmentTarget_Mirror3.stl)
and affixed with blue painter's tape and marked using the [aperture](stl/LaserCutterParts-P_AlignmentTarget_ScribeAperture.stl) and [aperture](stl/LaserCutterParts-P_AlignmentTarget_Scribe.stl) marking jigs so that objective measurements can be made of beam position at each point in the beam path.

Source models for each of these parts can be found in
the [FreeCAD file](LaserCutterParts.FCStd) in case modifications to the models
are required.


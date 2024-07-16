import textwrap
import pandas as pd
from datetime import datetime

class Generator:
    def __init__(self, sequence_name: str, save_path: str) -> None:
        self.file = ""
        self.sequence_name = sequence_name
        self.save_path = save_path

    def initial_header(self) -> None:
        fn = f"""
        <?xml version='1.0' standalone='yes' ?>
        <LVData xmlns="http://www.ni.com/LVData">
        <Version>8.6.1</Version>
        <String>
        <Name>XML Format Version</Name>
        <Val>1.0</Val>
        </String>
        <Cluster>
        <Name>Sequence Info</Name>
        <NumElts>4</NumElts>
        <String>
        <Name>Sequence Name</Name>
        <Val>{self.sequence_name}</Val>
        </String>
        <String>
        <Name>Sequence Description</Name>
        <Val></Val>
        </String>
        <String>
        <Name>Creation Date</Name>
        <Val>{datetime.now().strftime("%d/%m/%Y")}</Val>
        </String>
        <U16>
        <Name>Repetition</Name>
        <Val>1</Val>
        </U16>
        </Cluster>
        """
        self.file = "".join([self.file, fn])

    def move_absolute(self, axis: int, value: float, speed: float) -> None:
        fn = f"""<Cluster>
        <Name>Function info for XML file</Name>
        <NumElts>6</NumElts>
        <I32>
        <Name>Stage Axis index</Name>
        <Val>{axis}</Val>
        </I32>
        <I32>
        <Name>Load Cell Axis index</Name>
        <Val>0</Val>
        </I32>
        <String>
        <Name>Function</Name>
        <Val>Move Absolute</Val>
        </String>
        <Path>
        <Name>File Path</Name>
        <Val>{self.save_path}</Val>
        </Path>
        <Boolean>
        <Name>Data File Filter</Name>
        <Val>0</Val>
        </Boolean>
        <Cluster>
        <Name>Data file filter Parameters</Name>
        <NumElts>5</NumElts>
        <DBL>
        <Name>Time criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        <I32>
        <Name>Stage Axis</Name>
        <Val>0</Val>
        </I32>
        <DBL>
        <Name>Displacement criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        <I32>
        <Name>Load cell Axis</Name>
        <Val>0</Val>
        </I32>
        <DBL>
        <Name>Loading criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        </Cluster>
        </Cluster>
        <Cluster>
        <Name>Absolute move controls</Name>
        <NumElts>2</NumElts>
        <DBL>
        <Name>Position, $p</Name>
        <Val>{value}</Val>
        </DBL>
        <DBL>
        <Name>Velocity, $p/s</Name>
        <Val>{speed}</Val>
        </DBL>
        </Cluster>
        """
        self.file = "".join([self.file, fn])

    def find_contact(self, contact_criteria: float = 0.5, stage_velocity: float = 0.3, stage_limit: float = 20.0, repositioning: int = 1) -> None:
        fn = f"""<Cluster>
        <Name>Function info for XML file</Name>
        <NumElts>6</NumElts>
        <I32>
        <Name>Stage Axis index</Name>
        <Val>0</Val>
        </I32>
        <I32>
        <Name>Load Cell Axis index</Name>
        <Val>0</Val>
        </I32>
        <String>
        <Name>Function</Name>
        <Val>Find Contact</Val>
        </String>
        <Path>
        <Name>File Path</Name>
        <Val>{self.save_path}</Val>
        </Path>
        <Boolean>
        <Name>Data File Filter</Name>
        <Val>0</Val>
        </Boolean>
        <Cluster>
        <Name>Data file filter Parameters</Name>
        <NumElts>5</NumElts>
        <DBL>
        <Name>Time criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        <I32>
        <Name>Stage Axis</Name>
        <Val>0</Val>
        </I32>
        <DBL>
        <Name>Displacement criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        <I32>
        <Name>Load cell Axis</Name>
        <Val>0</Val>
        </I32>
        <DBL>
        <Name>Loading criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        </Cluster>
        </Cluster>
        <Cluster>
        <Name>Find contact controls</Name>
        <NumElts>6</NumElts>
        <EW>
        <Name>Direction</Name>
        <Choice>Positive</Choice>
        <Choice>Negative</Choice>
        <Val>0</Val>
        </EW>
        <DBL>
        <Name>Stage Velocity, $p/s</Name>
        <Val>{stage_velocity}</Val>
        </DBL>
        <DBL>
        <Name>Contact Criteria, $l</Name>
        <Val>{contact_criteria}</Val>
        </DBL>
        <DBL>
        <Name>Stage Limit, $p</Name>
        <Val>{stage_limit}</Val>
        </DBL>
        <EW>
        <Name>Stage Repositioning</Name>
        <Choice>None</Choice>
        <Choice>Stop Criteria + Offset</Choice>
        <Choice>2X Load Resolution</Choice>
        <Val>{repositioning}</Val>
        </EW>
        <DBL>
        <Name>Offset, $p</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        </Cluster>
        """
        self.file = "".join([self.file, fn])

    def ramp_release(self, ramp_amplitude: float = 4.6e-2, velocity_1: float = 4.6e-2, relax_time_1: float = 1.0, velocity_2: float = 4.6e-2, relax_time_2: float = 5.0) -> None:
        fn = f"""<Cluster>
        <Name>Function info for XML file</Name>
        <NumElts>6</NumElts>
        <I32>
        <Name>Stage Axis index</Name>
        <Val>0</Val>
        </I32>
        <I32>
        <Name>Load Cell Axis index</Name>
        <Val>0</Val>
        </I32>
        <String>
        <Name>Function</Name>
        <Val>Ramp-Release</Val>
        </String>
        <Path>
        <Name>File Path</Name>
        <Val>{self.save_path}</Val>
        </Path>
        <Boolean>
        <Name>Data File Filter</Name>
        <Val>0</Val>
        </Boolean>
        <Cluster>
        <Name>Data file filter Parameters</Name>
        <NumElts>5</NumElts>
        <DBL>
        <Name>Time criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        <I32>
        <Name>Stage Axis</Name>
        <Val>0</Val>
        </I32>
        <DBL>
        <Name>Displacement criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        <I32>
        <Name>Load cell Axis</Name>
        <Val>0</Val>
        </I32>
        <DBL>
        <Name>Loading criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        </Cluster>
        </Cluster>
        <Cluster>
        <Name>Ramp-Release controls</Name>
        <NumElts>6</NumElts>
        <DBL>
        <Name>Ramp Amplitude, $p</Name>
        <Val>{ramp_amplitude}</Val>
        </DBL>
        <DBL>
        <Name>Velocity 1, $p/s</Name>
        <Val>{velocity_1}</Val>
        </DBL>
        <DBL>
        <Name>Fixed Relaxation Time 1, s</Name>
        <Val>{relax_time_1}</Val>
        </DBL>
        <DBL>
        <Name>Velocity 2, $p/s</Name>
        <Val>{velocity_2}</Val>
        </DBL>
        <DBL>
        <Name>Fixed Relaxation Time 2, s</Name>
        <Val>{relax_time_2}</Val>
        </DBL>
        <U16>
        <Name>Number of Ramps</Name>
        <Val>5</Val>
        </U16>
        </Cluster>
        """
        self.file = "".join([self.file, fn])

    def wait(self, time: float = 600.0) -> None:
        fn = f"""<Cluster>
        <Name>Function info for XML file</Name>
        <NumElts>6</NumElts>
        <I32>
        <Name>Stage Axis index</Name>
        <Val>0</Val>
        </I32>
        <I32>
        <Name>Load Cell Axis index</Name>
        <Val>0</Val>
        </I32>
        <String>
        <Name>Function</Name>
        <Val>Wait</Val>
        </String>
        <Path>
        <Name>File Path</Name>
        <Val>{self.save_path}</Val>
        </Path>
        <Boolean>
        <Name>Data File Filter</Name>
        <Val>0</Val>
        </Boolean>
        <Cluster>
        <Name>Data file filter Parameters</Name>
        <NumElts>5</NumElts>
        <DBL>
        <Name>Time criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        <I32>
        <Name>Stage Axis</Name>
        <Val>0</Val>
        </I32>
        <DBL>
        <Name>Displacement criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        <I32>
        <Name>Load cell Axis</Name>
        <Val>0</Val>
        </I32>
        <DBL>
        <Name>Loading criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        </Cluster>
        </Cluster>
        <DBL>
        <Name>Time</Name>
        <Val>{time}</Val>
        </DBL>
        """
        self.file = "".join([self.file, fn])

    def stress_relaxation(self, ramp_amplitude: float = 0.115, ramp_velocity: float = 2.3, ramp_number: int = 3, relaxation_rate: float = 1e-2, relaxation_time: float = 900, slope_time: float = 10) -> None:
        fn = f"""<Cluster>
        <Name>Function info for XML file</Name>
        <NumElts>6</NumElts>
        <I32>
        <Name>Stage Axis index</Name>
        <Val>0</Val>
        </I32>
        <I32>
        <Name>Load Cell Axis index</Name>
        <Val>0</Val>
        </I32>
        <String>
        <Name>Function</Name>
        <Val>Stress Relaxation</Val>
        </String>
        <Path>
        <Name>File Path</Name>
        <Val>{self.save_path}</Val>
        </Path>
        <Boolean>
        <Name>Data File Filter</Name>
        <Val>0</Val>
        </Boolean>
        <Cluster>
        <Name>Data file filter Parameters</Name>
        <NumElts>5</NumElts>
        <DBL>
        <Name>Time criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        <I32>
        <Name>Stage Axis</Name>
        <Val>0</Val>
        </I32>
        <DBL>
        <Name>Displacement criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        <I32>
        <Name>Load cell Axis</Name>
        <Val>0</Val>
        </I32>
        <DBL>
        <Name>Loading criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        </Cluster>
        </Cluster>
        <Cluster>
        <Name>Stress relaxation controls</Name>
        <NumElts>7</NumElts>
        <DBL>
        <Name>Ramp Amplitude, $p</Name>
        <Val>{ramp_amplitude}</Val>
        </DBL>
        <DBL>
        <Name>Ramp Velocity, $p/s</Name>
        <Val>{ramp_velocity}</Val>
        </DBL>
        <U16>
        <Name>Number of Ramps</Name>
        <Val>{ramp_number}</Val>
        </U16>
        <EW>
        <Name>Stop based on</Name>
        <Choice>Fixed Relaxation Time</Choice>
        <Choice>Relaxation Rate</Choice>
        <Val>0</Val>
        </EW>
        <U16>
        <Name>Fixed Relaxation Time, s</Name>
        <Val>{relaxation_time}</Val>
        </U16>
        <DBL>
        <Name>Relaxation Rate, $l/min</Name>
        <Val>{relaxation_rate}</Val>
        </DBL>
        <U16>
        <Name>Time for Measurement of the Slope, s</Name>
        <Val>{slope_time}</Val>
        </U16>
        </Cluster>
        """
        self.file = "".join([self.file, fn])

    def sinusoid(self, amplitude: float = 4.6e-2, frequency: float = 0.25, cycles: int = 10) -> None:
        fn = f"""<Cluster>
        <Name>Function info for XML file</Name>
        <NumElts>6</NumElts>
        <I32>
        <Name>Stage Axis index</Name>
        <Val>0</Val>
        </I32>
        <I32>
        <Name>Load Cell Axis index</Name>
        <Val>0</Val>
        </I32>
        <String>
        <Name>Function</Name>
        <Val>Sinusoid</Val>
        </String>
        <Path>
        <Name>File Path</Name>
        <Val>{self.save_path}</Val>
        </Path>
        <Boolean>
        <Name>Data File Filter</Name>
        <Val>0</Val>
        </Boolean>
        <Cluster>
        <Name>Data file filter Parameters</Name>
        <NumElts>5</NumElts>
        <DBL>
        <Name>Time criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        <I32>
        <Name>Stage Axis</Name>
        <Val>0</Val>
        </I32>
        <DBL>
        <Name>Displacement criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        <I32>
        <Name>Load cell Axis</Name>
        <Val>0</Val>
        </I32>
        <DBL>
        <Name>Loading criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        </Cluster>
        </Cluster>
        <Cluster>
        <Name>Sinusoid controls</Name>
        <NumElts>3</NumElts>
        <DBL>
        <Name>Sinusoid Amplitude, $p</Name>
        <Val>{amplitude}</Val>
        </DBL>
        <DBL>
        <Name>Frequency, Hz</Name>
        <Val>{frequency}</Val>
        </DBL>
        <U16>
        <Name>Cycles</Name>
        <Val>{cycles}</Val>
        </U16>
        </Cluster>
        """
        self.file = "".join([self.file, fn])

    def zero_load(self) -> None:
        fn = f"""<Cluster>
        <Name>Function info for XML file</Name>
        <NumElts>6</NumElts>
        <I32>
        <Name>Stage Axis index</Name>
        <Val>2</Val>
        </I32>
        <I32>
        <Name>Load Cell Axis index</Name>
        <Val>0</Val>
        </I32>
        <String>
        <Name>Function</Name>
        <Val>Zero Load</Val>
        </String>
        <Path>
        <Name>File Path</Name>
        <Val>{self.save_path}</Val>
        </Path>
        <Boolean>
        <Name>Data File Filter</Name>
        <Val>0</Val>
        </Boolean>
        <Cluster>
        <Name>Data file filter Parameters</Name>
        <NumElts>5</NumElts>
        <DBL>
        <Name>Time criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        <I32>
        <Name>Stage Axis</Name>
        <Val>0</Val>
        </I32>
        <DBL>
        <Name>Displacement criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        <I32>
        <Name>Load cell Axis</Name>
        <Val>0</Val>
        </I32>
        <DBL>
        <Name>Loading criteria</Name>
        <Val>0.00000000000000</Val>
        </DBL>
        </Cluster>
        </Cluster>
        <String>
        <Name>Function Inputs</Name>
        <Val>None</Val>
        </String>
        """
        self.file = "".join([self.file, fn])

    def footer(self) -> None:
        fn = "</LVData>"
        self.file = "".join([self.file, fn])

    def save(self, file: str) -> None:
        with open(file, "w") as file_data:
            file_data.write(textwrap.dedent(self.file))


if __name__ == "__main__":
    save_path = r"C:\DATA\Akuroma\BOV01_R/"
    seq = Generator(sequence_name="Eloi Test", save_path=save_path)

    data = pd.read_excel("Resources/test_excel.xlsx")

    # Initial file header
    seq.initial_header()

    # For every point in the Excel file, perform this functions below
    for i in range(len(data)):
        # Update the save path value to match the data file
        seq.save_path = (save_path + str(data.iloc[i,1]) + ".txt").replace("/", r"\\")

        # Move Absolute
        seq.move_absolute(axis=1, value=data.iloc[i,6], speed=3.0)
        seq.move_absolute(axis=2, value=data.iloc[i,7], speed=3.0)

        # Zero Load
        if i == 0: seq.zero_load()

        # Find Contact
        seq.find_contact()

        # Ramp Release
        seq.ramp_release(ramp_amplitude=data.iloc[i,4], velocity_1=data.iloc[i,4], velocity_2=data.iloc[i,4])

        # Wait
        seq.wait()

        # Stress Relaxation
        seq.stress_relaxation(ramp_amplitude=data.iloc[i,5], ramp_velocity=data.iloc[i,3])

        # Sinusoid
        seq.sinusoid(amplitude=data.iloc[i,4], frequency=0.25)
        seq.sinusoid(amplitude=data.iloc[i,4], frequency=0.5)
        seq.sinusoid(amplitude=data.iloc[i,4], frequency=1)
        seq.sinusoid(amplitude=data.iloc[i,4], frequency=2)

        # Z Axis Home
        seq.move_absolute(axis=0, value=0, speed=0.3)


    seq.footer()
    seq.save("Resources/EloiTest.xml")

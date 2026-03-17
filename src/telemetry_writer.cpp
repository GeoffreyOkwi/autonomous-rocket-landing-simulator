#include "telemetry_writer.h"

TelemetryWriter::TelemetryWriter(const std::string& filename)
{
    file.open(filename);
}

void TelemetryWriter::writeHeader()
{
    file << "time,altitude,velocity,acceleration,fuel,throttle\n";
}

void TelemetryWriter::log(double time,
                          double altitude,
                          double velocity,
                          double acceleration,
                          double fuel,
                          double throttle)
{
    file << time << ","
         << altitude << ","
         << velocity << ","
         << acceleration << ","
         << fuel << ","
         << throttle << "\n";
}
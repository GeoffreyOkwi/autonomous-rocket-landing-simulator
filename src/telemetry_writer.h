#ifndef TELEMETRY_WRITER_H
#define TELEMETRY_WRITER_H

#include <fstream>

class TelemetryWriter
{
public:
    TelemetryWriter(const std::string& filename);

    void writeHeader();

    void log(double time,
             double altitude,
             double velocity,
             double acceleration,
             double fuel,
             double throttle);

private:
    std::ofstream file;
};

#endif
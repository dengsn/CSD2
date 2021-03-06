#ifndef OPERATOR_H
#define OPERATOR_H

#include "Oscillator.h"
#include <string>

class Operator
{
  protected:
    // Variables
    double amplitude;
    double phase;

  public:
    Operator(double amplitude = 1.0, double phase = 0.0);
    virtual ~Operator();

    // Getters and setters
    double getAmplitude();
    void setAmplitude(double amplitude);
    double getPhase();
    void setPhase(double phase);

    // Dynamic getter and setter for the prompt
    virtual double get(std::string parameter);
    virtual void set(std::string parameter, double value);

    // Convert this operator to an oscillator with a base frequency
    virtual Oscillator* convert(int sampleRate, double baseFrequency) = 0;

    // Create a string representation for this operator
    virtual std::string toString() = 0;
};

#endif // OPERATOR_H

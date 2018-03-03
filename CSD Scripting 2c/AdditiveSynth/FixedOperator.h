#ifndef FIXEDOPERATOR_H
#define FIXEDOPERATOR_H

#include "Operator.h"
#include "Oscillator.h"

class FixedOperator : public Operator
{
  protected:
    // Variables
    double frequency;

  public:
    FixedOperator(double frequency, double amplitude = 1.0, double phase = 0.0);
    virtual ~FixedOperator();

    // Getters and setters
    double getFrequency();
    void setFrequency(double ratio);

    // Convert this operator to an oscillator with a base frequency
    Oscillator* convert(int sampleRate, double baseFrequency);
};

#endif // FIXEDOPERATOR_H

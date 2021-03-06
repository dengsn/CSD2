#ifndef PATTERN_H
#define PATTERN_H

#include <string>

enum class PatternStatus
{
  IDLE,
  QUEUED_FOR_PLAYING,
  PLAYING,
  QUEUED_FOR_RECORDING,
  RECORDING
};

class Pattern
{
  private:
    // Variables
    PatternStatus status;
    unsigned int numBars;

  public:
    Pattern(unsigned int numBars);
    ~Pattern();

    // Getters and setters
    PatternStatus getStatus();
    void setStatus(PatternStatus status);
    unsigned int getNumBars();
    void setNumBars(unsigned int numBars);

    // Convert to string
    std::string toString();
};

#endif // PATTERN_H

#ifndef TIMELINE_H
#define TIMELINE_H

#include <vector>
#include <string>
#include "Pattern.h"

#define CHUNKSIZE 2048

enum class TimelineStatus
{
  IDLE,
  PLAYING
};

class Timeline
{
  private:
    // Variables
    std::vector<Pattern*> patterns;
    unsigned int beatsPerMinute;
    unsigned int beatsPerBar;

    unsigned int currentBeat;

  public:
    Timeline(unsigned int beatsPerMinute, unsigned int beatsPerBar);
    ~Timeline();

    //  Reset the time line
    void reset();

    // Getters and setters
    unsigned int getBeatsPerMinute();
    void setBeatsPerMinute(unsigned int beatsPerMinute);
    unsigned int getBeatsPerBar();
    void setBeatsPerBar(unsigned int beatsPerBar);

    // Pattern management
    void addPattern(Pattern* pattern);
    void removePattern(Pattern* pattern);
    Pattern* getPattern(int index);
    int patternCount();

    // Tick one beat forward
    void beat();

    // Convert to string
    std::string toString();
};

#endif // TIMELINE_H

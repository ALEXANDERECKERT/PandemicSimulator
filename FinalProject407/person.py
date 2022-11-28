class Person:

  def __init__(self, infectionStatus, turnsRemaining, immunityRemaining,infectionsCaused,vaccineStatus,vaccineSuccessRate,vaccineIntroductionRound):
    # 0 = uninfected, 1 = infected, 2 = immune
    self.infectionStatus = infectionStatus
    self.turnsRemaining = turnsRemaining
    self.immunityRemaining = immunityRemaining
    self.infectionsCaused = infectionsCaused
    self.vaccineStatus = vaccineStatus
    self.vaccineSuccessRate = vaccineSuccessRate
    self.vaccineIntroductionRound = vaccineIntroductionRound

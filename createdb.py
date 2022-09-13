from espinox import Token, db
import datetime
from datetime import date

currentTime = datetime.datetime.utcnow()

def setExpirationDate(currentT, licenseLengthInYears):
    return currentT.replace(year = currentT.month+licenseLengthInYears)

print(Token.query.get(123))
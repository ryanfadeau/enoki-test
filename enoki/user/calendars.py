from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, EasterMonday, Easter
from pandas.tseries.offsets import Day

class FrBusinessCalendar(AbstractHolidayCalendar):
    """
      - 1 Janvier: Jour de l'an
      - Lundi de pâque (Monday after Easter Sunday)
      - 1 Mai: Fête du travail
      - 8 Mai: Victoire des alliés 1954
      - Jeudi de l'Ascension (Thursday, 39 days after Easter Sunday)
      - 14 Juillet: Fếte nationale
      - 15 Août: Assomption
      - 1 Novembre: Toussaint
      - 11 Novembre: Armistice
      - 25 Décembre: Noël
    """
    rules = [
        Holiday("Jour de l'an", month=1, day=1),
        EasterMonday,
        Holiday('Fête du travail', month=5, day=1),
        Holiday('Victoire des alliés 1954', month=5, day=8),
        Holiday("Jeudi de l'Ascension", month=1, day=1, offset=[Easter(), Day(39)]),
        Holiday('Fếte nationale', month=7, day=14),
        Holiday('Assomption', month=8, day=15),
        Holiday('Toussaint', month=11, day=1),
        Holiday('Armistice 1918', month=11, day=11),
        Holiday('Noël', month=12, day=25)
    ]
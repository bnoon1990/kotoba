from datetime import datetime, timedelta
from .models import Card, Grade
from dataclasses import replace

class InvalidGradeError(ValueError):
    pass

def schedule(card: Card, grade: Grade, now: datetime) -> Card:
    
    # the algorythm based on SM-2
    match grade:
        case Grade.GOOD | Grade.EASY:
            match card.repetitions:
                case 0:
                    new_interval_days = 1
                case 1:
                    new_interval_days = 6
                case _:
                    new_interval_days = round(card.interval_days * card.ease)
            new_repetitions = card.repetitions + 1
        case Grade.AGAIN | Grade.HARD:
            new_repetitions = 0
            new_interval_days = 1
        case _:
            raise InvalidGradeError("Sorry, invalid grade")
            

    new_easiness = card.ease + (0.1 - (5 - grade) * (0.08 + (5 - grade) * 0.02))
    
    new_easiness = max(new_easiness, 1.3)

    new_due = now + timedelta(days=new_interval_days)

    return replace(card, ease=new_easiness, repetitions=new_repetitions, interval_days=new_interval_days, due=new_due) 



from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")

        if not vaccine:
            raise NotVaccinatedError(f"Visitor {self.name} is not vaccinated!")

        expiration_date = vaccine.get("expiration_date")
        if expiration_date < date.today():
            raise OutdatedVaccineError(f"Visitor {self.name}'s has expired!")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"Visitor {self.name} is not wearing a mask!"
            )

        return f"Welcome to {self.name}"

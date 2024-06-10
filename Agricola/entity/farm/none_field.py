"""
null값의 역할을 수행하는 noneField
"""
from Agricola_Back.Agricola.entity.animal_type import AnimalType
from Agricola_Back.Agricola.entity.farm.field import Field
from Agricola_Back.Agricola.entity.field_type import FieldType


class NoneField(Field):
    def __init__(self):
        self.field_type = FieldType.CAGE
        self.kind = None
        self.count = 0
        self.maximum = 0
        self.barn = False

""" Contains the Recipe Step Model """

from sqlalchemy import Column, BigInteger, ForeignKey, Text
from models.core.recipe import Recipe
from config import Config


class RecipeStep(Config.Base):
    """ Encapsulates a Recipe, it contains the user_id it belongs to """

    __tablename__ = 'recipe_step'

    id = Column(BigInteger, primary_key=True)
    recipe_id = Column(BigInteger, ForeignKey(Recipe.id))
    num = Column(BigInteger)
    description = Column(Text)


    def __repr__(self):
        return '<RecipeStep: {}>'.format(self.description)

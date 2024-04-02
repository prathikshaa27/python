from skincare.cleansers import Cleanser
from skincare.moisturizers import Moisturizer

class SkinCareRecommender:
    def recommend(self):
        cleanser= Cleanser("Foaming cleanser", 290,"Oily")
        moisturizer = Moisturizer("Ge based", 390, "Oily")

        print('Recommender cleanser:')
        cleanser.to_display_info()
        print('Recommender Moisturizer:')
        moisturizer.to_display_info()
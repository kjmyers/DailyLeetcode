class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        n = len(foods)
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings
        self.index = dict(zip(foods, range(n)))
        self.cuisinesMap = defaultdict(list)
        for i, cuisine in enumerate(cuisines):
            heappush(self.cuisinesMap[cuisine], (-self.ratings[i], self.foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        i = self.index[food]
        self.ratings[i] = newRating
        cuisine = self.cuisines[i]
        heappush(self.cuisinesMap[cuisine], (-self.ratings[i], self.foods[i]))


    def highestRated(self, cuisine: str) -> str:
        rating, food = self.cuisinesMap[cuisine][0]
        while rating != -self.ratings[self.index[food]]:  # check highest rating is current
            heappop(self.cuisinesMap[cuisine])
            rating, food = self.cuisinesMap[cuisine][0]
        return food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

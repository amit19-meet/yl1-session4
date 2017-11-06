class animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound= sound
		self.name= name
		self.age= age
		self.favorite_color= favorite_color

	def eat(self,food):
		print("Yummy!" + " " + self.name + " " + "is eating" + " " + food)

	def description(self):
		print(self.name + " " + "is" + " " + self.age + " " + "years old and loves the color" + " " + self.favorite_color)

	def make_sound(self, how_many_times):
		print(self.sound*how_many_times)



a= animal("meow ","Shakira","7","purple")
a.eat("marshmellow")
a.description()
a.make_sound(7)


class person(object):
	def __init__(self,name,age,city,gender):
		self.name= name
		self.age= age
		self.city= city
		self.gender= gender

	def eat(self, favorite_breakfast):
		print("Mmmm!" + " " + favorite_breakfast + " " + "is my favorite breakfast")

	def play(self, favorite_sport):
		print("Yayyyy!" + " " + favorite_sport + " " + "is my favorite sport")


m= person("Amit",16,"Kfar tavor", "female")
m.eat("pancakes")
m.play("dance")
from one_to_many import db, Pet, Person


# ######### to Create defined database
# db.create_all()

# ######### add new person
# omkar = Person(name= 'Omkar')
# db.session.add(omkar)
# db.session.commit()
# arnav = Person(name= 'Arnav')
# db.session.add(arnav)
# db.session.commit()
#
# ##### add with reference
# kalu = Pet(name="Kalu", owner=omkar)
# db.session.add(kalu)
# db.session.commit()
#
# moti = Pet(name="Moti", owner=omkar)
# db.session.add(moti)
# db.session.commit()


# ####### adding a pet from searching
# some_owner = Person.query.filter_by(name='Omkar').first()
# clifford = Pet(name='Clifford', owner=some_owner)
# db.session.add(clifford)
# db.session.commit()

# ###### getting pet ocject list from owner object
# # some_owner = Person.query.filter_by(name='Omkar').first()
# # print(some_owner.name, "Owns following pets")
# #
# # for pet in some_owner.pets: ## .pets will give all the pets object in list
# #     print(pet.name)

# ##### fetching owner object from pet object
# some_pet = Pet.query.filter_by(name='Kalu').first()
# print(some_pet.name)
# print()
# print(some_pet.owner.name) ###some_pet.owner will return owner object


####### Joins ############


#### Left outer join
# db.session.query()    ## this allows to set any query in slqalchemy
# left_join = db.session.query(Person, Pet).outerjoin(Pet, Person.id == Pet.owner_id).all()
# # print(left_join)
# for i in left_join[:-1]:
#     print(i[1].name)
#

#### right outer join
left_join = db.session.query(Person, Pet).outerjoin(Pet, Person.id == Pet.owner_id).all()
# print(left_join)
for i in left_join[:-1]:
    print(i[1].id,i[1].name, i[1].owner_id )
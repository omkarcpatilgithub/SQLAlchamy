from flaskalchemy import Example
from flaskalchemy import db


####### See all the results ########
# examples = Example.query.all()    # extract all values from the db
# for ex in examples:
#     print(ex.username)
###################################


####### Insert a data ##############
# new_ex = Example(5, "mandar")   # set new value to a variable
# db.session.add(new_ex)  # add it to database session
# db.session.commit()     # commit the session
###################################

####### Update a data #######
# update_test = Example.query.filter_by(id=3).first()    # pointing to the entry
# print(update_test.username)
# update_test.username = "Arnav Patil"      # update the entry
# db.session.commit()   # commit the entry
############################


####### Delete a data #######
## almost same as update
delete_test = Example.query.filter_by(id=2).first()
db.session.delete(delete_test)
db.session.commit()
############################

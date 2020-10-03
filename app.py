from sqlalchemy import create_engine,Column,Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()


### Defining a new table with columns id and username
class User(Base):
    __tablename__ = "person"

    id = Column('id',Integer, primary_key=True)
    username = Column('username', String, unique=True)

## Creating the table defined above
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

## creating a session,
## in a session we can add, remove our data and commit the session.
session = Session()

## adding one new entry inside the session
user = User()
user.id = 0
user.username = "omkar"
session.add(user)

# commit the session
session.commit()

# to see all the entries
users = session.query(User).all()
print(users)
for user in users:
    # print("user {} with id {}".format(user.username, user.id))
    print(" username=%s and id=%d" % (user.username, user.id))

# close the session
session.close()
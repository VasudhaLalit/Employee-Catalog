from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Department, Base

engine = create_engine('sqlite:///uemployeecatlog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

department1 = Department(dept_name='HR',user_id=1)
session.add(department1)
session.commit()

department2 = Department(dept_name='Finance',user_id=1)
session.add(department2)
session.commit()

department3 = Department(dept_name='Sales',user_id=1)
session.add(department3)
session.commit()

department4 = Department(dept_name='Marketing',user_id=1)
session.add(department4)
session.commit()

department5 = Department(dept_name='Information technology',user_id=1)
session.add(department5)
session.commit()

department6 = Department(dept_name='Admin',user_id=1)
session.add(department6)
session.commit()

department7 = Department(dept_name='Support',user_id=1)
session.add(department7)
session.commit()

print ('added all departments!')

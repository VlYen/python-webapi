import logging
from models.school_class_model import SchoolClassModel

logger = logging.getLogger(__name__)

class SqlLiteSchoolClassRepository:
   def __init__(self, connection):
      logger.info("Initializing SqlLiteProductRepository with provided connection.")
      if connection is None:
         logger.error("Connection cannot be None.")
         raise ValueError("Connection cannot be None.")
      self.connection = connection

   #--------------------------------------------------------------------
   def list_classes(self) -> list[SchoolClassModel]:
      try:
         # cursor = self.connection.cursor()
         import sqlite3

         db_path = "mydatabase.db"  # Adjust the path as needed
         local_conn=sqlite3.connect(db_path)
         query = "SELECT * FROM SchoolClasses"
         cursor = local_conn.cursor()
         cursor.execute(query)  
         rows = cursor.fetchall()
         return [SchoolClassModel(**dict(zip([column[0] for column in cursor.description], row))) for row in rows]
      except Exception as e:
         logger.error("Error occurred while listing students: %s", e)
         raise e
      finally:
         cursor.close()

   #--------------------------------------------------------------------
   def get_class_by_id(self, class_id) -> SchoolClassModel | None:
      try:
         cursor = self.connection.cursor()

         query = "SELECT * FROM SchoolClasses WHERE Id = ?"
         cursor.execute(query, (class_id,))  # Adjust the query as needed
         row = cursor.fetchone()
         if row:
            # The ** is Python's dictionary unpacking operator.
            return SchoolClassModel(**dict(zip([column[0] for column in cursor.description], row)))
         else:
            return None
      except Exception as e:
         logger.error("Error occurred while getting student by ID: %s", e)
         raise e
      finally:
         if cursor:
               cursor.close()

   #--------------------------------------------------------------------
   def create(self, school_class: SchoolClassModel) -> int:
      """
      Creates a new class and returns the new class's ID.

      :param:
         school_class (SchoolClassModel): The class data to insert.

      :return:
         int: The ID of the newly created class.
      """
      try:
         cursor = self.connection.cursor()
         query = """
            INSERT INTO SchoolClasses 
            (Name, Teacher, Room) 
            VALUES (?, ?, ?)
         """
         cursor.execute(query,
            (school_class.Name, school_class.Teacher, school_class.Room)
         )
         row = cursor.fetchone()
         self.connection.commit()
         return cursor.lastrowid
      except Exception as e:
         logger.error("Error occurred while creating class: %s", e)
         raise e
      finally:
         if cursor:
               cursor.close()               

   #--------------------------------------------------------------------
   def update(self, school_class: SchoolClassModel) -> int:
      """
      Updates an existing class.

      :param:
         school_class (SchoolClassModel): The class data to update.

      :return:
         int: The number of rows updated.
      """
      try:
         cursor = self.connection.cursor()
         query = """
            UPDATE SchoolClasses 
            SET Name = ?, Teacher = ?, Room = ? 
            WHERE Id = ?
         """ 
         cursor.execute(
               query,
               (school_class.Name, school_class.Teacher, school_class.Room, school_class.Id)
         )
         self.connection.commit()
         return cursor.rowcount  # Returns the number of rows updated
      except Exception as e:
         logger.error("Error occurred while updating class: %s", e)
         raise e
      finally:
         if cursor:
            cursor.close()

   #--------------------------------------------------------------------
   def delete(self, class_id: int) -> int:
      """
      Deletes a class by its ID.

      :param:
         class_id (int): The ID of the class to delete.

      :return:
         int: The number of rows deleted.
      """
      try:
         cursor = self.connection.cursor()

         query = "DELETE FROM SchoolClasses WHERE Id = ?"
         cursor.execute(query, (class_id,))
         self.connection.commit()
         logger.info(f"Deleted class with ID {class_id}, rows affected: {cursor.rowcount}")
         return cursor.rowcount  # Returns the number of rows deleted
      except Exception as e:
         logger.error("Error occurred while deleting class: %s", e)
         raise e
      finally:
         if cursor:
               cursor.close()
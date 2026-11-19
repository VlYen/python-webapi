import logging
from models.student_model import StudentModel

logger = logging.getLogger(__name__)

class SqlLiteStudentRepository:
   def __init__(self, connection):
      logger.info("Initializing SqlLiteProductRepository with provided connection.")
      if connection is None:
         logger.error("Connection cannot be None.")
         raise ValueError("Connection cannot be None.")
      self.connection = connection

   #--------------------------------------------------------------------
   def list_students(self) -> list[StudentModel]:
      try:
         # cursor = self.connection.cursor()
         import sqlite3

         db_path = "mydatabase.db"  # Adjust the path as needed
         local_conn=sqlite3.connect(db_path)
         query = "SELECT * FROM Students"
         cursor = local_conn.cursor()
         cursor.execute(query)  
         rows = cursor.fetchall()
         return [StudentModel(**dict(zip([column[0] for column in cursor.description], row))) for row in rows]
      except Exception as e:
         logger.error("Error occurred while listing students: %s", e)
         raise e
      finally:
         cursor.close()

   #--------------------------------------------------------------------
   def get_student_by_id(self, student_id) -> StudentModel | None:
      try:
         cursor = self.connection.cursor()

         query = "SELECT * FROM Students WHERE Id = ?"
         cursor.execute(query, (student_id,))  # Adjust the query as needed
         row = cursor.fetchone()
         if row:
            # The ** is Python's dictionary unpacking operator.
            return StudentModel(**dict(zip([column[0] for column in cursor.description], row)))
         else:
            return None
      except Exception as e:
         logger.error("Error occurred while getting student by ID: %s", e)
         raise e
      finally:
         if cursor:
               cursor.close()

   #--------------------------------------------------------------------
   def create(self, student: StudentModel) -> int:
      """
      Creates a new student and returns the new student's ID.

      :param:
         student (StudentModel): The student data to insert.

      :return:
         int: The ID of the newly created student.
      """
      try:
         cursor = self.connection.cursor()
         query = """
            INSERT INTO Students 
            (FirstName, LastName, SSN) 
            VALUES (?, ?, ?)
         """
         cursor.execute(query,
            (student.FirstName, student.LastName, student.SSN)
         )
         row = cursor.fetchone()
         self.connection.commit()
         return cursor.lastrowid
      except Exception as e:
         logger.error("Error occurred while creating student: %s", e)
         raise e
      finally:
         if cursor:
               cursor.close()               

   #--------------------------------------------------------------------
   def update(self, student: StudentModel) -> int:
      """
      Updates an existing student.

      :param:
         student (StudentModel): The student data to update.

      :return:
         int: The number of rows updated.
      """
      try:
         cursor = self.connection.cursor()
         query = """
            UPDATE Students 
            SET FirstName = ?, LastName = ?, SSN = ? 
            WHERE Id = ?
         """ 
         cursor.execute(
               query,
               (student.FirstName, student.LastName, student.SSN, student.Id)
         )
         self.connection.commit()
         return cursor.rowcount  # Returns the number of rows updated
      except Exception as e:
         logger.error("Error occurred while updating student: %s", e)
         raise e
      finally:
         if cursor:
            cursor.close()

   #--------------------------------------------------------------------
   def delete(self, student_id: int) -> int:
      """
      Deletes a student by its ID.

      :param:
         student_id (int): The ID of the student to delete.

      :return:
         int: The number of rows deleted.
      """
      try:
         cursor = self.connection.cursor()

         query = "DELETE FROM Students WHERE Id = ?"
         cursor.execute(query, (student_id,))
         self.connection.commit()
         logger.info(f"Deleted student with ID {student_id}, rows affected: {cursor.rowcount}")
         return cursor.rowcount  # Returns the number of rows deleted
      except Exception as e:
         logger.error("Error occurred while deleting student: %s", e)
         raise e
      finally:
         if cursor:
               cursor.close()
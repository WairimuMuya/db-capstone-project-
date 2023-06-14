CREATE DEFINER=`littleLemon`@`%` PROCEDURE `AddValidBooking`(IN TableNO INT, BookingDate DATE)
BEGIN
      BEGIN 
      START TRANSACTION; 
	  IF EXISTS (SELECT * FROM Bookings WHERE TableNO = TableNO AND BookingDate = BookingDate)
      THEN BEGIN
      SELECT concat("Table ", TableNO , " is already booked - Booking cancelled")  AS "Booking STATUS" ;
      ROLLBACK ; 
	  END; 
      ELSE 
      BEGIN
      INSERT INTO Bookings(TableNO, BookingDate)
      VALUES(TableNO, BookingDate);
      COMMIT;
      END;
      END IF;
      END; END
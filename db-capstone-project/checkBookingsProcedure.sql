CREATE DEFINER=`littleLemon`@`%` PROCEDURE `checkBooking`(IN TableNO INT, IN BookingDate DATE)
BEGIN
     IF EXISTS (SELECT * FROM Bookings WHERE TableNO = TableNO AND BookingDate = BookingDate)
     THEN BEGIN
     SELECT concat("Table ", TableNO , " is already booked")  AS "Booking STATUS" ;
	 END; 
     ELSE 
     BEGIN 
     INSERT INTO Bookings(TableNO, BookingDate)
     VALUES(TableNO, BookingDate);
     END;
     END IF; END
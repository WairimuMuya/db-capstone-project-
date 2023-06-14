CREATE DEFINER=`littleLemon`@`%` PROCEDURE `AddBooking`(IN BookingID INT, IN CustomerID INT, IN TableNO INT, BookingDate DATE)
BEGIN
    INSERT INTO bookings(BookingID, CustomerID, TableNO, BookingDate) VALUES (BookingID, CustomerID, TableNO, BookingDate);
    SELECT "New booking added" AS "CONFIRMATION";

END
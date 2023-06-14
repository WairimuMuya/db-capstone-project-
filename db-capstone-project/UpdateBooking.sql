CREATE DEFINER=`littleLemon`@`%` PROCEDURE `UpdateBooking`(IN BookingID INT, IN BookingDate DATE)
BEGIN
UPDATE bookings SET BookingDate = BookingDate WHERE BookingID = BookingID;
SELECT CONCAT('Booking ',BookingID, ' updated') AS CONFIRMATION;

END
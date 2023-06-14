CREATE DEFINER=`littleLemon`@`%` PROCEDURE `CancelBooking`(IN BookingID INT)
BEGIN
DELETE FROM bookings WHERE BookingDate = BookingDate;
SELECT CONCAT('Booking ',BookingID, ' cancelled') AS CONFIRMATION;
END
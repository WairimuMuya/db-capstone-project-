use littlelemondm;
prepare GetOrderDetail from 'select OrderID, Quantity, TotalCost from Orders where OrderID=?';

SET @id = 1;
EXECUTE GetOrderDetail USING @id;
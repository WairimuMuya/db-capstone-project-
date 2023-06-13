-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema LittleLemonDM
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema LittleLemonDM
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `LittleLemonDM` DEFAULT CHARACTER SET utf8 ;
USE `LittleLemonDM` ;

-- -----------------------------------------------------
-- Table `LittleLemonDM`.`CustomersDetails`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemonDM`.`CustomersDetails` (
  `CustomerID` INT NOT NULL AUTO_INCREMENT,
  `FullName` VARCHAR(255) NOT NULL,
  `ContactNumber` VARCHAR(45) NOT NULL,
  `Email` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`CustomerID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LittleLemonDM`.`StaffDetails`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemonDM`.`StaffDetails` (
  `EmployeeID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(255) NOT NULL,
  `Role` VARCHAR(255) NOT NULL,
  `Address` VARCHAR(255) NOT NULL,
  `ContactNO` INT NOT NULL,
  `Email` VARCHAR(100) NOT NULL,
  `AnnualSalary` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`EmployeeID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LittleLemonDM`.`Bookings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemonDM`.`Bookings` (
  `BookingID` INT NOT NULL AUTO_INCREMENT,
  `CustomerID` INT NOT NULL,
  `TableNO` INT NOT NULL,
  `BookingDate` DATE NOT NULL,
  `BookingSlot` TIME NOT NULL,
  `EmployeeID` INT NOT NULL,
  PRIMARY KEY (`BookingID`),
  INDEX `customer_id_idx` (`CustomerID` ASC) VISIBLE,
  INDEX `emmployee_id_idx` (`EmployeeID` ASC) VISIBLE,
  CONSTRAINT `customer_id`
    FOREIGN KEY (`CustomerID`)
    REFERENCES `LittleLemonDM`.`CustomersDetails` (`CustomerID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `emmployee_id`
    FOREIGN KEY (`EmployeeID`)
    REFERENCES `LittleLemonDM`.`StaffDetails` (`EmployeeID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LittleLemonDM`.`MenuItems`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemonDM`.`MenuItems` (
  `ItemID` INT NOT NULL,
  `Name` VARCHAR(255) NOT NULL,
  `Type` VARCHAR(45) NOT NULL,
  `Price` INT NOT NULL,
  PRIMARY KEY (`ItemID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LittleLemonDM`.` Menu`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemonDM`.` Menu` (
  `MenuID` INT NOT NULL AUTO_INCREMENT,
  `ItemID` INT NOT NULL,
  `Cuisine` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`MenuID`, `ItemID`),
  INDEX `Item_id_idx` (`ItemID` ASC) VISIBLE,
  CONSTRAINT `Item_id`
    FOREIGN KEY (`ItemID`)
    REFERENCES `LittleLemonDM`.`MenuItems` (`ItemID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LittleLemonDM`.`Orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemonDM`.`Orders` (
  `OrderID` INT NOT NULL AUTO_INCREMENT,
  `TableNO` INT NOT NULL,
  `MenuID` INT NOT NULL,
  `BookingID` INT NULL,
  `OrderDate` DATE NOT NULL,
  `Quantity` INT NOT NULL,
  `Price` INT NOT NULL,
  `TotalCost` INT NOT NULL,
  PRIMARY KEY (`OrderID`, `TableNO`),
  INDEX `menu_id_idx` (`MenuID` ASC) VISIBLE,
  INDEX `booking_id_idx` (`BookingID` ASC) VISIBLE,
  CONSTRAINT `menu_id`
    FOREIGN KEY (`MenuID`)
    REFERENCES `LittleLemonDM`.` Menu` (`MenuID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `booking_id`
    FOREIGN KEY (`BookingID`)
    REFERENCES `LittleLemonDM`.`Bookings` (`BookingID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LittleLemonDM`.`OrderDeliveryStatus`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LittleLemonDM`.`OrderDeliveryStatus` (
  `OrderID` INT NOT NULL,
  `Status` VARCHAR(45) NOT NULL,
  `DeliveryDate` DATE NOT NULL,
  PRIMARY KEY (`OrderID`),
  CONSTRAINT `order_id`
    FOREIGN KEY (`OrderID`)
    REFERENCES `LittleLemonDM`.`Orders` (`OrderID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema agro
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema agro
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `agro` DEFAULT CHARACTER SET utf8 ;
USE `agro` ;

-- -----------------------------------------------------
-- Table `agro`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `agro`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `agro`.`publicaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `agro`.`publicaciones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `finca` VARCHAR(255) NULL,
  `variedad` VARCHAR(45) NULL,
  `fertilizante` VARCHAR(45) NULL,
  `municipio` VARCHAR(255) NULL,
  `fecha_cosecha` DATE NULL,
  `numero_cosecha` INT NULL,
  `nombre_fertilizante` VARCHAR(255) NULL,
  `tipo_fertilizante` VARCHAR(45) NULL,
  `cantidad_fertilizante` FLOAT NULL,
  `enfermedades` VARCHAR(45) NULL,
  `frecuencia_enfermedad` INT NULL,
  `produccion` FLOAT NULL,
  `vereda` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `agro`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `agro`.`likes` (
  `users_id` INT NOT NULL,
  `publicaciones_id` INT NOT NULL,
  PRIMARY KEY (`users_id`, `publicaciones_id`),
  INDEX `fk_users_has_publicaciones_publicaciones1_idx` (`publicaciones_id` ASC) VISIBLE,
  INDEX `fk_users_has_publicaciones_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_publicaciones_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `agro`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_publicaciones_publicaciones1`
    FOREIGN KEY (`publicaciones_id`)
    REFERENCES `agro`.`publicaciones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `agro`.`comentarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `agro`.`comentarios` (
  `users_id` INT NOT NULL,
  `publicaciones_id` INT NOT NULL,
  PRIMARY KEY (`users_id`, `publicaciones_id`),
  INDEX `fk_users_has_publicaciones_publicaciones2_idx` (`publicaciones_id` ASC) VISIBLE,
  INDEX `fk_users_has_publicaciones_users1_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_publicaciones_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `agro`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_publicaciones_publicaciones2`
    FOREIGN KEY (`publicaciones_id`)
    REFERENCES `agro`.`publicaciones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

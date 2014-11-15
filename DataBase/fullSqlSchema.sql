SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

DROP SCHEMA IF EXISTS `pyInstructor` ;
CREATE SCHEMA IF NOT EXISTS `pyInstructor` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `pyInstructor` ;

-- -----------------------------------------------------
-- Table `pyInstructor`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pyInstructor`.`users` ;

CREATE TABLE IF NOT EXISTS `pyInstructor`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `firstName` VARCHAR(255) NOT NULL,
  `lastName` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `registered` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pyInstructor`.`topics`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pyInstructor`.`topics` ;

CREATE TABLE IF NOT EXISTS `pyInstructor`.`topics` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pyInstructor`.`questions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pyInstructor`.`questions` ;

CREATE TABLE IF NOT EXISTS `pyInstructor`.`questions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `questionText` TEXT NOT NULL,
  `topicId` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_questions_topics1_idx` (`topicId` ASC),
  CONSTRAINT `fk_questions_topics1`
    FOREIGN KEY (`topicId`)
    REFERENCES `pyInstructor`.`topics` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pyInstructor`.`profil`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pyInstructor`.`profil` ;

CREATE TABLE IF NOT EXISTS `pyInstructor`.`profil` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `profilPictureURL` VARCHAR(255) NULL,
  `city` VARCHAR(255) NULL,
  `address` VARCHAR(255) NULL,
  `phone` VARCHAR(100) NULL,
  `userId` INT NOT NULL,
  `birthday` DATE NULL,
  `privilidge` INT(1) NOT NULL DEFAULT 1 COMMENT '0- admin\n1- user',
  PRIMARY KEY (`id`),
  INDEX `fk_profil_users1_idx` (`userId` ASC),
  CONSTRAINT `fk_profil_users1`
    FOREIGN KEY (`userId`)
    REFERENCES `pyInstructor`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pyInstructor`.`results`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pyInstructor`.`results` ;

CREATE TABLE IF NOT EXISTS `pyInstructor`.`results` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `result` INT NOT NULL,
  `userId` INT NOT NULL,
  `topicId` INT NOT NULL,
  `examDate` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_results_users1_idx` (`userId` ASC),
  INDEX `fk_results_topics1_idx` (`topicId` ASC),
  CONSTRAINT `fk_results_users1`
    FOREIGN KEY (`userId`)
    REFERENCES `pyInstructor`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_results_topics1`
    FOREIGN KEY (`topicId`)
    REFERENCES `pyInstructor`.`topics` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pyInstructor`.`answers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pyInstructor`.`answers` ;

CREATE TABLE IF NOT EXISTS `pyInstructor`.`answers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `answerText` TEXT NOT NULL,
  `questionId` INT NOT NULL,
  `isItCorrect` TINYINT(1) NULL,
  `topicId` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_answers_questions1_idx` (`questionId` ASC),
  INDEX `fk_answers_topics1_idx` (`topicId` ASC),
  CONSTRAINT `fk_answers_questions1`
    FOREIGN KEY (`questionId`)
    REFERENCES `pyInstructor`.`questions` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_answers_topics1`
    FOREIGN KEY (`topicId`)
    REFERENCES `pyInstructor`.`topics` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pyInstructor`.`userAnswers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pyInstructor`.`userAnswers` ;

CREATE TABLE IF NOT EXISTS `pyInstructor`.`userAnswers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `questionId` INT NOT NULL,
  `answerId` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_userAnswers_questions1_idx` (`questionId` ASC),
  INDEX `fk_userAnswers_answers1_idx` (`answerId` ASC),
  CONSTRAINT `fk_userAnswers_questions1`
    FOREIGN KEY (`questionId`)
    REFERENCES `pyInstructor`.`questions` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_userAnswers_answers1`
    FOREIGN KEY (`answerId`)
    REFERENCES `pyInstructor`.`answers` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pyInstructor`.`topics_user_conn`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pyInstructor`.`topics_user_conn` ;

CREATE TABLE IF NOT EXISTS `pyInstructor`.`topics_user_conn` (
  `topicsId` INT NOT NULL,
  `usersId` INT NOT NULL,
  INDEX `fk_topics_has_users_users1_idx` (`usersId` ASC),
  INDEX `fk_topics_has_users_topics1_idx` (`topicsId` ASC),
  CONSTRAINT `fk_topics_has_users_topics1`
    FOREIGN KEY (`topicsId`)
    REFERENCES `pyInstructor`.`topics` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_topics_has_users_users1`
    FOREIGN KEY (`usersId`)
    REFERENCES `pyInstructor`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
